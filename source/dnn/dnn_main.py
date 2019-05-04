import sys
sys.path.append('.')

from PyQt5 import QtWidgets, QtGui, QtCore
from view.teacher_view import Ui_MainWindow
from feature_extractor import *

class mainWindow(QtWidgets.QMainWindow):
    dname = ""
    def __init__(self):
        super(mainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pb_path.clicked.connect(self.pathSelect)
        self.ui.pb_exctract.clicked.connect(self.extractFeatures)
    
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

app = QtWidgets.QApplication([])
win = mainWindow()
win.show()
sys.exit(app.exec())