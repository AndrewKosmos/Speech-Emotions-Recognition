# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recognizer_view.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 259)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.w_spec = QtWidgets.QWidget(self.centralwidget)
        self.w_spec.setObjectName("w_spec")
        self.gridLayout.addWidget(self.w_spec, 1, 1, 1, 1)
        self.pb_voice = QtWidgets.QPushButton(self.centralwidget)
        self.pb_voice.setObjectName("pb_voice")
        self.gridLayout.addWidget(self.pb_voice, 0, 1, 1, 1)
        self.w_waves = QtWidgets.QWidget(self.centralwidget)
        self.w_waves.setObjectName("w_waves")
        self.gridLayout.addWidget(self.w_waves, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.pb_open = QtWidgets.QPushButton(self.centralwidget)
        self.pb_open.setObjectName("pb_open")
        self.gridLayout.addWidget(self.pb_open, 0, 0, 1, 1)
        self.l_result = QtWidgets.QLabel(self.centralwidget)
        self.l_result.setText("")
        self.l_result.setObjectName("l_result")
        self.gridLayout.addWidget(self.l_result, 2, 0, 1, 1)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pb_voice.setText(_translate("MainWindow", "Запись голоса"))
        self.pb_open.setText(_translate("MainWindow", "Открыть файл"))

