import sys
sys.path.append('.')

from PyQt5 import QtWidgets, QtGui, QtCore
from view.teacher_view import Ui_MainWindow

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pb_path.clicked.connect(self.pathSelect)
    
    def pathSelect(self):
        dname = QtWidgets.QFileDialog.getExistingDirectory(self,"Select Directory")
        self.ui.le_path.setText(dname)

app = QtWidgets.QApplication([])
win = mainWindow()
win.show()
sys.exit(app.exec())