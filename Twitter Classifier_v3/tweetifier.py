# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tweetifier.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
import sys
from classifier import Classify
from preprocessed_tweets import first_level
from fetch_tweet import TweetFetch
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *

class Ui_MainWindow(object):

    def fromfile(self):
        self.fromfile  = TweetFetch()
        f = self.fromfile.fetchFromFile()
        self.textEdit.setText(f)
        self.textEdit_3.setText("Tweet Fetched from file")

    def fromtwitter(self):
        self.fromtwitter  = TweetFetch()
        self.fromtwitter.status()
        f = self.fromtwitter.fetchFromTwitter()
        self.textEdit.setText(f)
        self.textEdit_3.setText("Tweet Fetched from Twitter")

    def cl(self):
        self.cl = Classify()
        a = self.cl.classify_r1()
        self.textEdit_2.setText(a+' >>')
        b = self.cl.classify_r2(a)
        self.textEdit_2.append(b)
        self.textEdit_3.setText("Tweet Classfied")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(579, 458)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 140, 151, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.fromfile)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 300, 85, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.cl)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 130, 301, 101))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(220, 250, 301, 171))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setReadOnly(True)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 230, 611, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 541, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(220, 60, 301, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setReadOnly(True)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 110, 601, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 200, 151, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.fromtwitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Fetch Tweet from File"))
        self.pushButton_2.setText(_translate("MainWindow", "Classify"))
        self.label.setText(_translate("MainWindow", "Welcome to Twitter Classifier! This system classifies tweet into 3 level deep cateorization"))
        self.label_2.setText(_translate("MainWindow", "Status of Processing Request"))
        self.pushButton_3.setText(_translate("MainWindow", "Fetch Tweet from Twitter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

