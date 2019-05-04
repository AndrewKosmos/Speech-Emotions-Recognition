# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacher_view.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 175)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pb_path = QtWidgets.QPushButton(self.centralwidget)
        self.pb_path.setObjectName("pb_path")
        self.gridLayout.addWidget(self.pb_path, 1, 1, 1, 1)
        self.le_path = QtWidgets.QLineEdit(self.centralwidget)
        self.le_path.setObjectName("le_path")
        self.gridLayout.addWidget(self.le_path, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.pb_teach = QtWidgets.QPushButton(self.centralwidget)
        self.pb_teach.setObjectName("pb_teach")
        self.gridLayout.addWidget(self.pb_teach, 3, 0, 1, 2)
        self.pb_exctract = QtWidgets.QPushButton(self.centralwidget)
        self.pb_exctract.setObjectName("pb_exctract")
        self.gridLayout.addWidget(self.pb_exctract, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Обучающая программа"))
        self.label.setText(_translate("MainWindow", "Укажите путь до обучающей базы"))
        self.pb_path.setText(_translate("MainWindow", "Выбрать"))
        self.pb_teach.setText(_translate("MainWindow", "Обучить"))
        self.pb_exctract.setText(_translate("MainWindow", "Извлечь полезные данные"))

