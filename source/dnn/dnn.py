import glob
import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from matplotlib.pyplot import specgram
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from keras.models import load_model
from PyQt5 import QtCore

class Dnn(QtCore.QObject):
    model = None
    emotions = ['neutral', 'calm', 'happy', 'sad', 'angry', 'fear', 'disgust', 'surprised']
    def __init__(self, X_data, Y_data):
        self.X = X_data
        self.Y = Y_data

    def setParams(self, hidden_units1, hidden_units2, hidden_units3):
        self.train_x, self.test_x, self.train_y, self.test_y = train_test_split(self.X, self.Y, test_size=0.33, random_state=42)
        self.n_dim = self.train_x.shape[1]
        self.n_classes = self.train_y.shape[1]
        self.n_input   = self.n_dim
        self.n_hidden1 = hidden_units1
        self.n_hidden2 = hidden_units2
        self.n_hidden3 = hidden_units3
        self.n_output  = self.n_classes

    def create_model(self, activation_func='relu', init_type='normal', optimiser='adam', dropout_rate=0.2):
        self.model = Sequential()
        # Input layer
        self.model.add(Dense(self.n_input, input_dim=self.n_dim, init=init_type, activation=activation_func))
        
        # Hidden layer 1
        self.model.add(Dense(self.n_hidden1, init=init_type, activation=activation_func))
        self.model.add(Dropout(dropout_rate))

        # Hidden layer 2
        self.model.add(Dense(self.n_hidden2, init=init_type, activation=activation_func))
        self.model.add(Dropout(dropout_rate))

        # Hidden layer 3
        self.model.add(Dense(self.n_hidden3, init=init_type, activation=activation_func))
        self.model.add(Dropout(dropout_rate))

        # Output layer
        self.model.add(Dense(self.n_output, init=init_type, activation='softmax'))

        # Model compilation
        self.model.compile(loss='categorical_crossentropy', optimizer=optimiser, metrics=['accuracy'])

    def fit_model(self, save_filepath="models/model.h5", n_epochs=400, batch_s=4, is_verbose=1):
        self.model.fit(self.train_x, self.train_y, epochs=n_epochs, batch_size=batch_s, verbose=is_verbose)
        self.model.save(save_filepath)
        QtCore.qDebug("model saved!")

    def calcConfusionMatrix(self):
        prediction = self.model.predict(self.test_x, batch_size=4)
        label_predict = np.argmax(prediction, 1)
        predicted_emo = []

        for i in range(0, self.test_y.shape[0]):
            emotion = self.emotions[label_predict[i]]
            predicted_emo.append(emotion)

        actual_emo = []
        label_true = np.argmax(self.test_y, 1)
        for i in range(0, self.test_y.shape[0]):
            emo = self.emotions[label_true[i]]
            actual_emo.append(emo)

        confusion_mx = confusion_matrix(actual_emo, predicted_emo)
        index = ['angry', 'calm', 'disgust', 'fearful', 'happy', 'neutral', 'sad', 'surprised'] 
        columns = ['angry', 'calm', 'disgust', 'fearful', 'happy', 'neutral', 'sad', 'surprised'] 
        confusion_matrix_df = pd.DataFrame(confusion_mx, index, columns)
        plt.figure(figsize=(10,6))
        sns.heatmap(confusion_matrix_df, annot=True)
        plt.show()