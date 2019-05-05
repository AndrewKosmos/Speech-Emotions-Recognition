import sys
sys.path.append('.')

from PyQt5 import QtWidgets, QtGui, QtCore
from view.teacher_view import Ui_MainWindow
from feature_extractor import *
from dnn import *

class MainWindow(QtWidgets.QMainWindow):
    dname = ""
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pb_quality.setEnabled(False)

        self.ui.pb_path.clicked.connect(self.pathSelect)
        self.ui.pb_exctract.clicked.connect(self.extractFeatures)
        self.ui.pb_teach.clicked.connect(self.teachClicked)
    
    def pathSelect(self):
        self.dname = QtWidgets.QFileDialog.getExistingDirectory(self,"Select Directory")
        self.ui.le_path.setText(self.dname)

    def extractFeatures(self):
        QtCore.qDebug("Extract features from ")
        QtCore.qDebug(self.dname)
        sub_dirs = os.listdir(self.dname)
        features, labels = parse_files(self.dname, sub_dirs)
        np.save("models/X", features)
        labels = one_hot_encode(labels)
        np.save("models/Y", labels)
        QtCore.qDebug("Features were extracted")

    def teachClicked(self):
        QtCore.qDebug("TEACH!")
        self.ui.pb_quality.setEnabled(True)
        X_data = np.load("models/X.npy")
        Y_data = np.load("models/Y.npy")
        dnn = Dnn(X_data, Y_data)
        dnn.setParams(600, 300, 150)
        dnn.create_model()
        dnn.fit_model()
        

app = QtWidgets.QApplication([])
win = MainWindow()
win.show()
sys.exit(app.exec())