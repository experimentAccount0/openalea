# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/mainwindow.ui'
#
# Created: Wed Apr 30 15:19:02 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,779,662).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon(":/icons/openalea_icon.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.vboxlayout = QtGui.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setObjectName("vboxlayout")

        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")

        self.tabWidget = QtGui.QTabWidget(self.splitter)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.tab)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.vboxlayout1.addWidget(self.label_4)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.radioRecommended = QtGui.QRadioButton(self.tab)
        self.radioRecommended.setChecked(True)
        self.radioRecommended.setObjectName("radioRecommended")
        self.hboxlayout.addWidget(self.radioRecommended)

        self.radioAll = QtGui.QRadioButton(self.tab)
        self.radioAll.setObjectName("radioAll")
        self.hboxlayout.addWidget(self.radioAll)

        self.radioUpdate = QtGui.QRadioButton(self.tab)
        self.radioUpdate.setObjectName("radioUpdate")
        self.hboxlayout.addWidget(self.radioUpdate)

        self.radioInstalled = QtGui.QRadioButton(self.tab)
        self.radioInstalled.setObjectName("radioInstalled")
        self.hboxlayout.addWidget(self.radioInstalled)
        self.vboxlayout1.addLayout(self.hboxlayout)

        self.packageList = QtGui.QListWidget(self.tab)
        self.packageList.setAlternatingRowColors(True)
        self.packageList.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.packageList.setSortingEnabled(True)
        self.packageList.setObjectName("packageList")
        self.vboxlayout1.addWidget(self.packageList)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.checkAll = QtGui.QPushButton(self.tab)
        self.checkAll.setFlat(True)
        self.checkAll.setObjectName("checkAll")
        self.hboxlayout1.addWidget(self.checkAll)

        self.ClearAll = QtGui.QPushButton(self.tab)
        self.ClearAll.setFlat(True)
        self.ClearAll.setObjectName("ClearAll")
        self.hboxlayout1.addWidget(self.ClearAll)

        spacerItem = QtGui.QSpacerItem(521,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.vboxlayout1.addLayout(self.hboxlayout1)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.proceedButton = QtGui.QPushButton(self.tab)
        self.proceedButton.setObjectName("proceedButton")
        self.hboxlayout2.addWidget(self.proceedButton)

        self.refreshButton = QtGui.QPushButton(self.tab)
        self.refreshButton.setObjectName("refreshButton")
        self.hboxlayout2.addWidget(self.refreshButton)
        self.vboxlayout1.addLayout(self.hboxlayout2)
        self.tabWidget.addTab(self.tab,"")

        self.OtherEggs = QtGui.QWidget()
        self.OtherEggs.setObjectName("OtherEggs")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.OtherEggs)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.label = QtGui.QLabel(self.OtherEggs)
        self.label.setObjectName("label")
        self.vboxlayout2.addWidget(self.label)

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.requestEdit = QtGui.QLineEdit(self.OtherEggs)
        self.requestEdit.setObjectName("requestEdit")
        self.hboxlayout3.addWidget(self.requestEdit)

        self.fileButton = QtGui.QPushButton(self.OtherEggs)
        self.fileButton.setObjectName("fileButton")
        self.hboxlayout3.addWidget(self.fileButton)
        self.vboxlayout2.addLayout(self.hboxlayout3)

        spacerItem1 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout2.addItem(spacerItem1)

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.customInstallButton = QtGui.QPushButton(self.OtherEggs)
        self.customInstallButton.setObjectName("customInstallButton")
        self.hboxlayout4.addWidget(self.customInstallButton)
        self.vboxlayout2.addLayout(self.hboxlayout4)
        self.tabWidget.addTab(self.OtherEggs,"")

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.tab_2)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.vboxlayout3.addWidget(self.label_2)

        self.locationList = QtGui.QListWidget(self.tab_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.locationList.sizePolicy().hasHeightForWidth())
        self.locationList.setSizePolicy(sizePolicy)
        self.locationList.setObjectName("locationList")
        self.vboxlayout3.addWidget(self.locationList)

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setSpacing(6)
        self.hboxlayout5.setMargin(0)
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.addLocButton = QtGui.QPushButton(self.tab_2)
        self.addLocButton.setObjectName("addLocButton")
        self.hboxlayout5.addWidget(self.addLocButton)

        self.removeLocButton = QtGui.QPushButton(self.tab_2)
        self.removeLocButton.setObjectName("removeLocButton")
        self.hboxlayout5.addWidget(self.removeLocButton)
        self.vboxlayout3.addLayout(self.hboxlayout5)
        self.tabWidget.addTab(self.tab_2,"")

        self.customPackagePage = QtGui.QWidget()
        self.customPackagePage.setObjectName("customPackagePage")

        self.gridlayout = QtGui.QGridLayout(self.customPackagePage)
        self.gridlayout.setObjectName("gridlayout")

        self.label_5 = QtGui.QLabel(self.customPackagePage)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5,0,0,1,5)

        self.label_6 = QtGui.QLabel(self.customPackagePage)
        self.label_6.setObjectName("label_6")
        self.gridlayout.addWidget(self.label_6,1,0,1,1)

        self.customPackageNameEdit = QtGui.QLineEdit(self.customPackagePage)
        self.customPackageNameEdit.setObjectName("customPackageNameEdit")
        self.gridlayout.addWidget(self.customPackageNameEdit,1,1,1,4)

        self.label_7 = QtGui.QLabel(self.customPackagePage)
        self.label_7.setObjectName("label_7")
        self.gridlayout.addWidget(self.label_7,2,0,1,1)

        self.customPackageVersionEdit = QtGui.QLineEdit(self.customPackagePage)
        self.customPackageVersionEdit.setObjectName("customPackageVersionEdit")
        self.gridlayout.addWidget(self.customPackageVersionEdit,2,1,1,1)

        spacerItem2 = QtGui.QSpacerItem(291,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem2,2,2,1,2)

        self.label_8 = QtGui.QLabel(self.customPackagePage)
        self.label_8.setObjectName("label_8")
        self.gridlayout.addWidget(self.label_8,3,0,1,1)

        self.customPackageDirEdit = QtGui.QLineEdit(self.customPackagePage)
        self.customPackageDirEdit.setObjectName("customPackageDirEdit")
        self.gridlayout.addWidget(self.customPackageDirEdit,3,1,1,3)

        self.customPackageDirButton = QtGui.QPushButton(self.customPackagePage)
        self.customPackageDirButton.setObjectName("customPackageDirButton")
        self.gridlayout.addWidget(self.customPackageDirButton,3,4,1,1)

        self.customPackageIncludeFrame = QtGui.QGroupBox(self.customPackagePage)
        self.customPackageIncludeFrame.setEnabled(True)
        self.customPackageIncludeFrame.setCheckable(True)
        self.customPackageIncludeFrame.setChecked(False)
        self.customPackageIncludeFrame.setObjectName("customPackageIncludeFrame")

        self.hboxlayout6 = QtGui.QHBoxLayout(self.customPackageIncludeFrame)
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.label_9 = QtGui.QLabel(self.customPackageIncludeFrame)
        self.label_9.setObjectName("label_9")
        self.hboxlayout6.addWidget(self.label_9)

        self.customPackageIncludeEdit = QtGui.QLineEdit(self.customPackageIncludeFrame)
        self.customPackageIncludeEdit.setObjectName("customPackageIncludeEdit")
        self.hboxlayout6.addWidget(self.customPackageIncludeEdit)

        self.customPackageIncludeButton = QtGui.QPushButton(self.customPackageIncludeFrame)
        self.customPackageIncludeButton.setObjectName("customPackageIncludeButton")
        self.hboxlayout6.addWidget(self.customPackageIncludeButton)
        self.gridlayout.addWidget(self.customPackageIncludeFrame,4,0,1,5)

        self.customPackageLibFrame = QtGui.QGroupBox(self.customPackagePage)
        self.customPackageLibFrame.setCheckable(True)
        self.customPackageLibFrame.setChecked(False)
        self.customPackageLibFrame.setObjectName("customPackageLibFrame")

        self.hboxlayout7 = QtGui.QHBoxLayout(self.customPackageLibFrame)
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.label_11 = QtGui.QLabel(self.customPackageLibFrame)
        self.label_11.setObjectName("label_11")
        self.hboxlayout7.addWidget(self.label_11)

        self.customPackageLibEdit = QtGui.QLineEdit(self.customPackageLibFrame)
        self.customPackageLibEdit.setObjectName("customPackageLibEdit")
        self.hboxlayout7.addWidget(self.customPackageLibEdit)

        self.customPackageLibButton = QtGui.QPushButton(self.customPackageLibFrame)
        self.customPackageLibButton.setObjectName("customPackageLibButton")
        self.hboxlayout7.addWidget(self.customPackageLibButton)
        self.gridlayout.addWidget(self.customPackageLibFrame,5,0,1,5)

        spacerItem3 = QtGui.QSpacerItem(20,20,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem3,6,3,1,1)

        spacerItem4 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem4,7,2,1,1)

        self.customResetButton = QtGui.QPushButton(self.customPackagePage)
        self.customResetButton.setObjectName("customResetButton")
        self.gridlayout.addWidget(self.customResetButton,7,3,1,1)

        self.customApplyButton = QtGui.QPushButton(self.customPackagePage)
        self.customApplyButton.setObjectName("customApplyButton")
        self.gridlayout.addWidget(self.customApplyButton,7,4,1,1)
        self.tabWidget.addTab(self.customPackagePage,"")

        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")

        self.vboxlayout4 = QtGui.QVBoxLayout(self.layoutWidget)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.vboxlayout4.addWidget(self.label_3)

        self.logText = QtGui.QTextEdit(self.layoutWidget)
        self.logText.setReadOnly(True)
        self.logText.setObjectName("logText")
        self.vboxlayout4.addWidget(self.logText)
        self.vboxlayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,779,21))
        self.menubar.setObjectName("menubar")

        self.menuAuthentification = QtGui.QMenu(self.menubar)
        self.menuAuthentification.setObjectName("menuAuthentification")

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.actionCookie_Session = QtGui.QAction(MainWindow)
        self.actionCookie_Session.setObjectName("actionCookie_Session")

        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")

        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName("action_About")

        self.action_Web = QtGui.QAction(MainWindow)
        self.action_Web.setObjectName("action_Web")
        self.menuAuthentification.addAction(self.actionCookie_Session)
        self.menu_File.addAction(self.action_Quit)
        self.menuHelp.addAction(self.action_About)
        self.menuHelp.addAction(self.action_Web)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuAuthentification.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget,self.radioRecommended)
        MainWindow.setTabOrder(self.radioRecommended,self.radioAll)
        MainWindow.setTabOrder(self.radioAll,self.radioUpdate)
        MainWindow.setTabOrder(self.radioUpdate,self.radioInstalled)
        MainWindow.setTabOrder(self.radioInstalled,self.packageList)
        MainWindow.setTabOrder(self.packageList,self.checkAll)
        MainWindow.setTabOrder(self.checkAll,self.ClearAll)
        MainWindow.setTabOrder(self.ClearAll,self.proceedButton)
        MainWindow.setTabOrder(self.proceedButton,self.refreshButton)
        MainWindow.setTabOrder(self.refreshButton,self.logText)
        MainWindow.setTabOrder(self.logText,self.requestEdit)
        MainWindow.setTabOrder(self.requestEdit,self.fileButton)
        MainWindow.setTabOrder(self.fileButton,self.customInstallButton)
        MainWindow.setTabOrder(self.customInstallButton,self.locationList)
        MainWindow.setTabOrder(self.locationList,self.addLocButton)
        MainWindow.setTabOrder(self.addLocButton,self.removeLocButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "OpenAlea Installer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Packages</span> : Select the packages you want to install/update/remove and click on <span style=\" font-weight:600;\">Install/Remove</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.radioRecommended.setText(QtGui.QApplication.translate("MainWindow", "Install Recommended packages", None, QtGui.QApplication.UnicodeUTF8))
        self.radioAll.setText(QtGui.QApplication.translate("MainWindow", "Install All packages", None, QtGui.QApplication.UnicodeUTF8))
        self.radioUpdate.setText(QtGui.QApplication.translate("MainWindow", " Update packages", None, QtGui.QApplication.UnicodeUTF8))
        self.radioInstalled.setText(QtGui.QApplication.translate("MainWindow", "Remove packages", None, QtGui.QApplication.UnicodeUTF8))
        self.checkAll.setText(QtGui.QApplication.translate("MainWindow", "CheckAll", None, QtGui.QApplication.UnicodeUTF8))
        self.ClearAll.setText(QtGui.QApplication.translate("MainWindow", "ClearAll", None, QtGui.QApplication.UnicodeUTF8))
        self.proceedButton.setText(QtGui.QApplication.translate("MainWindow", "Install/Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.refreshButton.setText(QtGui.QApplication.translate("MainWindow", "Refresh List", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Install/Remove OpenAlea Packages", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Enter  : </span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  + a Python<span style=\" font-style:italic;\"> package name </span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  + or the <span style=\" font-style:italic;\">URL of an Egg</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  + or the <span style=\" font-style:italic;\">local path of an Egg</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.fileButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.customInstallButton.setText(QtGui.QApplication.translate("MainWindow", "Install", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.OtherEggs), QtGui.QApplication.translate("MainWindow", "Install Other Eggs", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Locations </span>: repository URLs</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.addLocButton.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.removeLocButton.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Repository", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "<b>Custom Package:</b> To declare in the package database a local version of a package", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Package name :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Version : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Directory :", None, QtGui.QApplication.UnicodeUTF8))
        self.customPackageDirButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.customPackageIncludeFrame.setTitle(QtGui.QApplication.translate("MainWindow", "Include", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Directory :", None, QtGui.QApplication.UnicodeUTF8))
        self.customPackageIncludeButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.customPackageLibFrame.setTitle(QtGui.QApplication.translate("MainWindow", "Lib", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Directory :", None, QtGui.QApplication.UnicodeUTF8))
        self.customPackageLibButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.customResetButton.setText(QtGui.QApplication.translate("MainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.customApplyButton.setText(QtGui.QApplication.translate("MainWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.customPackagePage), QtGui.QApplication.translate("MainWindow", "Custom Local Package", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Log</span> : System Output</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAuthentification.setTitle(QtGui.QApplication.translate("MainWindow", "&Authentification", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCookie_Session.setText(QtGui.QApplication.translate("MainWindow", "INRIA GForge Session", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Web.setText(QtGui.QApplication.translate("MainWindow", "&Web", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
