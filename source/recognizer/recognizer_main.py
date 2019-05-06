import sys
sys.path.append('.')

from PyQt5 import QtWidgets, QtGui, QtCore
from view.recognizer_view import Ui_MainWindow
from source.dnn.dnn import *
from source.dnn.feature_extractor import *
from source.recognizer.graphWidget import *

class MainWindow(QtWidgets.QMainWindow):
    model = None
    fname = ""
    emotions=['neutral', 'calm', 'happy', 'sad', 'angry', 'fearful', 'disgust', 'surprised']
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pb_open.clicked.connect(self.load_file)
        self.model = load_model("models/model.h5")

    def load_file(self):
        if self.model is not None:
            self.fname, cat = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", "", "All Files (*);; Wav files (*.wav)")
            
            try:
                mfcc, chroma, mel, contrast, tonnetz = extract_features(self.fname)
                print("Featuers successfully extracted")
            except Exception as e:
                print("Error while parsing file!")

            # Draw graphs
            o_file, sr = librosa.load(self.fname)
            fig = plt.figure(figsize=(1.5,1.5))
            plt.subplot(2,1,1)
            librosa.display.waveplot(np.array(o_file),sr=22050)
            self.comp = QtWidgets.QVBoxLayout(self.ui.w_waves)
            self.canv = MatplotGraphWidget(fig)
            self.comp.addWidget(self.canv)

            # Prediction
            features = np.empty((193,0))
            extracted_features = np.hstack([mfcc, chroma, mel, contrast, tonnetz])
            features = np.array(extracted_features)
            features = features.reshape(1,193)
            predict = self.model.predict(features, batch_size=4)
            print(predict)
            y_pred = np.argmax(predict, 1)
            emotion = self.emotions[y_pred[0]]
            self.ui.l_result.setText(emotion)



app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())