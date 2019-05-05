import sys
sys.path.append('.')

from PyQt5 import QtWidgets, QtGui, QtCore
from view.recognizer_view import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())