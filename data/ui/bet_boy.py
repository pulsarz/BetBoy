# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bet_boy.ui'
#
# Created: Mon May 13 17:29:28 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_BetTools(object):
    def setupUi(self, BetTools):
        BetTools.setObjectName("BetTools")
        BetTools.resize(631, 417)
        BetTools.setStyleSheet("")
        self.centralwidget = QtGui.QWidget(BetTools)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setStyleSheet("")
        self.mdiArea.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mdiArea.setFrameShadow(QtGui.QFrame.Raised)
        self.mdiArea.setLineWidth(0)
        self.mdiArea.setMidLineWidth(0)
        self.mdiArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        brush = QtGui.QBrush(QtGui.QColor(184, 184, 184))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setActivationOrder(QtGui.QMdiArea.StackingOrder)
        self.mdiArea.setViewMode(QtGui.QMdiArea.TabbedView)
        self.mdiArea.setDocumentMode(False)
        self.mdiArea.setTabsClosable(True)
        self.mdiArea.setTabsMovable(True)
        self.mdiArea.setTabShape(QtGui.QTabWidget.Triangular)
        self.mdiArea.setTabPosition(QtGui.QTabWidget.North)
        self.mdiArea.setObjectName("mdiArea")
        self.horizontalLayout.addWidget(self.mdiArea)
        BetTools.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(BetTools)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 631, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuTools = QtGui.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        BetTools.setMenuBar(self.menuBar)
        self.actionStats_central = QtGui.QAction(BetTools)
        self.actionStats_central.setObjectName("actionStats_central")
        self.actionSimulator = QtGui.QAction(BetTools)
        self.actionSimulator.setObjectName("actionSimulator")
        self.actionUpdate_manager = QtGui.QAction(BetTools)
        self.actionUpdate_manager.setObjectName("actionUpdate_manager")
        self.actionLinks_creator = QtGui.QAction(BetTools)
        self.actionLinks_creator.setObjectName("actionLinks_creator")
        self.actionLeagues_creator = QtGui.QAction(BetTools)
        self.actionLeagues_creator.setObjectName("actionLeagues_creator")
        self.actionExport_manager = QtGui.QAction(BetTools)
        self.actionExport_manager.setObjectName("actionExport_manager")
        self.actionLearning_manager = QtGui.QAction(BetTools)
        self.actionLearning_manager.setObjectName("actionLearning_manager")
        self.actionAbout = QtGui.QAction(BetTools)
        self.actionAbout.setObjectName("actionAbout")
        self.actionMatch_selector = QtGui.QAction(BetTools)
        self.actionMatch_selector.setObjectName("actionMatch_selector")
        self.menuTools.addAction(self.actionStats_central)
        self.menuTools.addAction(self.actionMatch_selector)
        self.menuTools.addAction(self.actionSimulator)
        self.menuTools.addAction(self.actionUpdate_manager)
        self.menuTools.addAction(self.actionLinks_creator)
        self.menuTools.addAction(self.actionLeagues_creator)
        self.menuTools.addAction(self.actionExport_manager)
        self.menuTools.addAction(self.actionLearning_manager)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(BetTools)
        QtCore.QMetaObject.connectSlotsByName(BetTools)

    def retranslateUi(self, BetTools):
        BetTools.setWindowTitle(QtGui.QApplication.translate("BetTools", "BetBoy", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("BetTools", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("BetTools", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStats_central.setText(QtGui.QApplication.translate("BetTools", "Stats central", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSimulator.setText(QtGui.QApplication.translate("BetTools", "Simulator", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate_manager.setText(QtGui.QApplication.translate("BetTools", "Update manager", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLinks_creator.setText(QtGui.QApplication.translate("BetTools", "Links creator", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLeagues_creator.setText(QtGui.QApplication.translate("BetTools", "Leagues creator", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_manager.setText(QtGui.QApplication.translate("BetTools", "Export manager", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLearning_manager.setText(QtGui.QApplication.translate("BetTools", "Learning manager", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("BetTools", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMatch_selector.setText(QtGui.QApplication.translate("BetTools", "Match selector", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
