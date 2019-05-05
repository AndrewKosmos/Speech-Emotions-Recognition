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

def extract_features(file_name):
    data, sample_rate = librosa.load(file_name)
    stft = np.abs(librosa.stft(data))
    # Вычисление мел-кепстральных коэффициентов
    mfcc = np.mean(librosa.feature.mfcc(y=data, sr=sample_rate, n_mfcc=40).T, axis=0)
    # Вычисление хроматограммы по форме волны или спектрограмме мощности
    chroma_stft = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
    # Вычисление масштабированной спектрограмму мощности мел
    mel_specgram = np.mean(librosa.feature.melspectrogram(data, sr=sample_rate).T, axis=0)
    # Вычисление спектрального контраста
    spectral_contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T, axis=0)
    # Вычисление функций центра тяжести тона
    tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(data), sr=sample_rate).T, axis=0)
    
    return mfcc, chroma_stft, mel_specgram, spectral_contrast, tonnetz

def parse_files(parent_dir, sub_dirs, file_ext="*.wav"):
    features, labels = np.empty((0,193)), np.empty(0)
    for label, sub_dir in enumerate(sub_dirs):
        for file_name in glob.glob(os.path.join(parent_dir, sub_dir, file_ext)):
            print(file_name)
            try:
                mfcc, c_stft, mel_spec, spec_contrast, tonnetz = extract_features(file_name)
                print("File parsed successfully")
            except Exception as e:
                print("Error while parsing file!")
                continue
            extracted_features = np.hstack([mfcc, c_stft, mel_spec, spec_contrast, tonnetz])
            features = np.vstack([features, extracted_features])
            labels = np.append(labels, file_name.split('/')[7].split('-')[2])
    return np.array(features), np.array(labels, dtype=np.int)

def one_hot_encode(labels):
    n_labels = len(labels)
    n_uniq_labels = len(np.unique(labels))
    one_hot_encode = np.zeros((n_labels, n_uniq_labels + 1))
    one_hot_encode[np.arange(n_labels), labels] = 1
    one_hot_encode = np.delete(one_hot_encode, 0, axis=1)
    return one_hot_encode