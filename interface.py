# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("STranslate")
        MainWindow.setEnabled(True)
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        self.centralWidget.setStyleSheet("background-color: rgb(251, 252, 187);")
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainFrame = QtWidgets.QFrame(self.centralWidget)
        self.mainFrame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.mainFrame.setStyleSheet("background-color: rgb(230, 229, 255)")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mainFrame.setLineWidth(3)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.inputLayout = QtWidgets.QHBoxLayout()
        self.inputLayout.setObjectName("inputLayout")
        self.inputFrame = QtWidgets.QFrame(self.mainFrame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(239, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.inputFrame.setPalette(palette)
        self.inputFrame.setAutoFillBackground(False)
        self.inputFrame.setStyleSheet("background-color: rgb(239, 255, 255)")
        self.inputFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.inputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inputFrame.setLineWidth(4)
        self.inputFrame.setObjectName("inputFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.inputFrame)
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.input = QtWidgets.QPlainTextEdit(self.inputFrame)
        self.input.setStyleSheet("background-color: rgb(255, 250, 240)")
        self.input.setFrameShape(QtWidgets.QFrame.Panel)
        self.input.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.input.setLineWidth(3)
        self.input.setObjectName("input")
        self.verticalLayout_4.addWidget(self.input)
        self.inputLayout.addWidget(self.inputFrame)
        self.mainLayout.addLayout(self.inputLayout)
        self.langFrame = QtWidgets.QFrame(self.mainFrame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(245, 255, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 255, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 255, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 255, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 255, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 255, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 255, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 255, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 255, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.langFrame.setPalette(palette)
        self.langFrame.setStyleSheet("background-color: rgb(245, 255, 240)")
        self.langFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.langFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.langFrame.setLineWidth(4)
        self.langFrame.setObjectName("langFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.langFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.langLayout = QtWidgets.QHBoxLayout()
        self.langLayout.setContentsMargins(50, -1, 50, -1)
        self.langLayout.setObjectName("langLayout")
        self.labelTranslateFrom = QtWidgets.QLabel(self.langFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTranslateFrom.sizePolicy().hasHeightForWidth())
        self.labelTranslateFrom.setSizePolicy(sizePolicy)
        self.labelTranslateFrom.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTranslateFrom.setObjectName("labelTranslateFrom")
        self.langLayout.addWidget(self.labelTranslateFrom)
        self.langFrom = QtWidgets.QComboBox(self.langFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.langFrom.sizePolicy().hasHeightForWidth())
        self.langFrom.setSizePolicy(sizePolicy)
        self.langFrom.setObjectName("langFrom")
        self.langFrom.addItem("")
        self.langFrom.addItem("")
        self.langLayout.addWidget(self.langFrom)
        self.labelTranslateTo = QtWidgets.QLabel(self.langFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTranslateTo.sizePolicy().hasHeightForWidth())
        self.labelTranslateTo.setSizePolicy(sizePolicy)
        self.labelTranslateTo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTranslateTo.setObjectName("labelTranslateTo")
        self.langLayout.addWidget(self.labelTranslateTo)
        self.langTo = QtWidgets.QComboBox(self.langFrame)
        self.langTo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.langTo.sizePolicy().hasHeightForWidth())
        self.langTo.setSizePolicy(sizePolicy)
        self.langTo.setEditable(False)
        self.langTo.setObjectName("langTo")
        self.langTo.addItem("")
        self.langTo.addItem("")
        self.langLayout.addWidget(self.langTo)
        self.verticalLayout_3.addLayout(self.langLayout)
        self.mainLayout.addWidget(self.langFrame)
        self.translateBtnLayout = QtWidgets.QHBoxLayout()
        self.translateBtnLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.translateBtnLayout.setObjectName("translateBtnLayout")
        self.translateBtn = QtWidgets.QPushButton(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.translateBtn.sizePolicy().hasHeightForWidth())
        self.translateBtn.setSizePolicy(sizePolicy)
        self.translateBtn.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.translateBtn.setFont(font)
        self.translateBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.translateBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.translateBtn.setAutoFillBackground(False)
        self.translateBtn.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.translateBtn.setAutoDefault(False)
        self.translateBtn.setDefault(False)
        self.translateBtn.setFlat(False)
        self.translateBtn.setObjectName("translateBtn")
        self.translateBtnLayout.addWidget(self.translateBtn)
        self.mainLayout.addLayout(self.translateBtnLayout)
        self.outputLayout = QtWidgets.QHBoxLayout()
        self.outputLayout.setContentsMargins(-1, -1, -1, 0)
        self.outputLayout.setObjectName("outputLayout")
        self.outputFrame = QtWidgets.QFrame(self.mainFrame)
        self.outputFrame.setStyleSheet("background-color: rgb(239, 255, 255)")
        self.outputFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.outputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputFrame.setLineWidth(4)
        self.outputFrame.setObjectName("outputFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.outputFrame)
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.output = QtWidgets.QPlainTextEdit(self.outputFrame)
        self.output.setEnabled(True)
        self.output.setStyleSheet("background-color: rgb(255, 250, 240)")
        self.output.setFrameShape(QtWidgets.QFrame.Panel)
        self.output.setLineWidth(3)
        self.output.setObjectName("output")
        self.verticalLayout_5.addWidget(self.output)
        self.outputLayout.addWidget(self.outputFrame)
        self.mainLayout.addLayout(self.outputLayout)
        self.verticalLayout.addLayout(self.mainLayout)
        self.horizontalLayout.addWidget(self.mainFrame)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.Help = QtWidgets.QMenu(self.menubar)
        self.Help.setObjectName("Help")
        self.settings = QtWidgets.QMenu(self.menubar)
        self.settings.setObjectName("settings")
        MainWindow.setMenuBar(self.menubar)
        self.about = QtWidgets.QAction(MainWindow)
        self.about.setObjectName("about")
        self.creator = QtWidgets.QAction(MainWindow)
        self.creator.setObjectName("creator")
        self.standard = QtWidgets.QAction(MainWindow)
        self.standard.setObjectName("standard")
        self.mini = QtWidgets.QAction(MainWindow)
        self.mini.setObjectName("mini")
        self.dictionaries = QtWidgets.QAction(MainWindow)
        self.dictionaries.setObjectName("dictionaries")
        self.help_quit = QtWidgets.QAction(MainWindow)
        self.help_quit.setObjectName("help_quit")
        self.Help.addAction(self.about)
        self.Help.addAction(self.creator)
        self.Help.addAction(self.help_quit)
        self.settings.addAction(self.dictionaries)
        self.menubar.addAction(self.settings.menuAction())
        self.menubar.addAction(self.Help.menuAction())

        self.retranslateUi(MainWindow)
        self.langFrom.setCurrentIndex(1)
        self.langTo.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTranslateFrom.setText(_translate("MainWindow", "C"))
        self.langFrom.setCurrentText(_translate("MainWindow", "Русского"))
        self.langFrom.setItemText(0, _translate("MainWindow", "Английского"))
        self.langFrom.setItemText(1, _translate("MainWindow", "Русского"))
        self.labelTranslateTo.setText(_translate("MainWindow", "На"))
        self.langTo.setItemText(0, _translate("MainWindow", "Русский"))
        self.langTo.setItemText(1, _translate("MainWindow", "Английский"))
        self.translateBtn.setText(_translate("MainWindow", "Перевести"))
        self.Help.setTitle(_translate("MainWindow", "Помощь"))
        self.settings.setTitle(_translate("MainWindow", "Настройки"))
        self.about.setText(_translate("MainWindow", "О программе"))
        self.creator.setText(_translate("MainWindow", "О разработчике"))
        self.standard.setText(_translate("MainWindow", "Обычный"))
        self.mini.setText(_translate("MainWindow", "Мини"))
        self.dictionaries.setText(_translate("MainWindow", "Словари"))
        self.help_quit.setText(_translate("MainWindow", "Выйти из программы"))
