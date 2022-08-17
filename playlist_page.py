# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playlist_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_playlist_page(object):
    def setupUi(self, playlist_page):
        playlist_page.setObjectName("playlist_page")
        playlist_page.resize(1071, 681)
        playlist_page.setStyleSheet("")
        self.frame = QtWidgets.QFrame(playlist_page)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1071, 681))
        self.frame.setStyleSheet("#frame{\n"
"background-color:rgba(20,21,28,255);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1071, 681))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.playlist_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.playlist_label.setStyleSheet("#playlist_label{\n"
"background-color:rgba(18,19,25,255);\n"
"color:rgba(253,253,254,255);\n"
"border-radius:5px;\n"
"text-align:left;\n"
"font: 15pt \"Russo One\";\n"
"margin-top: 20px;\n"
"margin-left:20px;\n"
"}")
        self.playlist_label.setObjectName("playlist_label")
        self.verticalLayout.addWidget(self.playlist_label)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("background-color:rgba(18,19,25,255);\n"
"color:rgba(253,253,254,255);\n"
"border-radius:5px;\n"
"text-align:left;\n"
"font: 15pt \"Russo One\";\n"
"margin-top: 20px;\n"
"margin-left:20px;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(playlist_page)
        QtCore.QMetaObject.connectSlotsByName(playlist_page)

    def retranslateUi(self, playlist_page):
        _translate = QtCore.QCoreApplication.translate
        playlist_page.setWindowTitle(_translate("playlist_page", "Form"))
        self.playlist_label.setText(_translate("playlist_page", "Play List"))
        self.label.setText(_translate("playlist_page", "Test"))