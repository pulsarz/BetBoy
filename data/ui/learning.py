# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'learning.ui'
#
# Created: Mon May 13 17:29:28 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Learn(object):
    def setupUi(self, Learn):
        Learn.setObjectName("Learn")
        Learn.resize(645, 525)
        self.horizontalLayout_9 = QtGui.QHBoxLayout(Learn)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tree_exports = QtGui.QTreeWidget(Learn)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_exports.sizePolicy().hasHeightForWidth())
        self.tree_exports.setSizePolicy(sizePolicy)
        self.tree_exports.setMaximumSize(QtCore.QSize(250, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tree_exports.setPalette(palette)
        self.tree_exports.setObjectName("tree_exports")
        self.tree_exports.headerItem().setText(0, "1")
        self.verticalLayout_3.addWidget(self.tree_exports)
        self.button_exp_delete = QtGui.QPushButton(Learn)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/actions/actions/editdelete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_exp_delete.setIcon(icon)
        self.button_exp_delete.setObjectName("button_exp_delete")
        self.verticalLayout_3.addWidget(self.button_exp_delete)
        self.line_learn = QtGui.QLineEdit(Learn)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_learn.sizePolicy().hasHeightForWidth())
        self.line_learn.setSizePolicy(sizePolicy)
        self.line_learn.setMaximumSize(QtCore.QSize(250, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.line_learn.setPalette(palette)
        self.line_learn.setObjectName("line_learn")
        self.verticalLayout_3.addWidget(self.line_learn)
        self.button_learn = QtGui.QPushButton(Learn)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_learn.sizePolicy().hasHeightForWidth())
        self.button_learn.setSizePolicy(sizePolicy)
        self.button_learn.setMaximumSize(QtCore.QSize(250, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/actions/actions/wizard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_learn.setIcon(icon1)
        self.button_learn.setObjectName("button_learn")
        self.verticalLayout_3.addWidget(self.button_learn)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tree_nets = QtGui.QTreeWidget(Learn)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_nets.sizePolicy().hasHeightForWidth())
        self.tree_nets.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tree_nets.setPalette(palette)
        self.tree_nets.setObjectName("tree_nets")
        self.tree_nets.headerItem().setText(0, "1")
        self.verticalLayout_4.addWidget(self.tree_nets)
        self.button_delete = QtGui.QPushButton(Learn)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_delete.sizePolicy().hasHeightForWidth())
        self.button_delete.setSizePolicy(sizePolicy)
        self.button_delete.setMaximumSize(QtCore.QSize(250, 16777215))
        self.button_delete.setIcon(icon)
        self.button_delete.setObjectName("button_delete")
        self.verticalLayout_4.addWidget(self.button_delete)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(Learn)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spin_hidden = QtGui.QSpinBox(Learn)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.spin_hidden.setPalette(palette)
        self.spin_hidden.setMinimum(1)
        self.spin_hidden.setMaximum(999999)
        self.spin_hidden.setSingleStep(10)
        self.spin_hidden.setProperty("value", 30)
        self.spin_hidden.setObjectName("spin_hidden")
        self.horizontalLayout.addWidget(self.spin_hidden)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(Learn)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spin_error = QtGui.QDoubleSpinBox(Learn)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.spin_error.setPalette(palette)
        self.spin_error.setDecimals(6)
        self.spin_error.setMinimum(0.0)
        self.spin_error.setMaximum(1.0)
        self.spin_error.setSingleStep(0.001)
        self.spin_error.setProperty("value", 1e-06)
        self.spin_error.setObjectName("spin_error")
        self.horizontalLayout_2.addWidget(self.spin_error)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(Learn)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.spin_epochs = QtGui.QSpinBox(Learn)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.spin_epochs.setPalette(palette)
        self.spin_epochs.setMinimum(100)
        self.spin_epochs.setMaximum(1000000)
        self.spin_epochs.setSingleStep(500)
        self.spin_epochs.setProperty("value", 1000)
        self.spin_epochs.setObjectName("spin_epochs")
        self.horizontalLayout_3.addWidget(self.spin_epochs)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtGui.QLabel(Learn)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.spin_rate = QtGui.QDoubleSpinBox(Learn)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.spin_rate.setPalette(palette)
        self.spin_rate.setMaximum(1.0)
        self.spin_rate.setSingleStep(0.1)
        self.spin_rate.setProperty("value", 0.6)
        self.spin_rate.setObjectName("spin_rate")
        self.horizontalLayout_4.addWidget(self.spin_rate)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtGui.QLabel(Learn)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.spin_reports = QtGui.QSpinBox(Learn)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.spin_reports.setPalette(palette)
        self.spin_reports.setMinimum(10)
        self.spin_reports.setMaximum(1000)
        self.spin_reports.setSingleStep(10)
        self.spin_reports.setProperty("value", 10)
        self.spin_reports.setObjectName("spin_reports")
        self.horizontalLayout_5.addWidget(self.spin_reports)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtGui.QLabel(Learn)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.combo_algorithm = QtGui.QComboBox(Learn)
        self.combo_algorithm.setObjectName("combo_algorithm")
        self.combo_algorithm.addItem("")
        self.combo_algorithm.addItem("")
        self.combo_algorithm.addItem("")
        self.combo_algorithm.addItem("")
        self.horizontalLayout_6.addWidget(self.combo_algorithm)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtGui.QLabel(Learn)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.combo_hidden = QtGui.QComboBox(Learn)
        self.combo_hidden.setObjectName("combo_hidden")
        self.combo_hidden.addItem("")
        self.combo_hidden.addItem("")
        self.combo_hidden.addItem("")
        self.combo_hidden.addItem("")
        self.combo_hidden.addItem("")
        self.combo_hidden.addItem("")
        self.combo_hidden.addItem("")
        self.combo_hidden.addItem("")
        self.combo_hidden.addItem("")
        self.combo_hidden.addItem("")
        self.combo_hidden.addItem("")
        self.combo_hidden.addItem("")
        self.combo_hidden.addItem("")
        self.combo_hidden.addItem("")
        self.combo_hidden.addItem("")
        self.combo_hidden.addItem("")
        self.horizontalLayout_7.addWidget(self.combo_hidden)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtGui.QLabel(Learn)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.combo_output = QtGui.QComboBox(Learn)
        self.combo_output.setObjectName("combo_output")
        self.combo_output.addItem("")
        self.combo_output.addItem("")
        self.combo_output.addItem("")
        self.combo_output.addItem("")
        self.combo_output.addItem("")
        self.combo_output.addItem("")
        self.combo_output.addItem("")
        self.combo_output.addItem("")
        self.combo_output.addItem("")
        self.combo_output.addItem("")
        self.combo_output.addItem("")
        self.combo_output.addItem("")
        self.combo_output.addItem("")
        self.combo_output.addItem("")
        self.combo_output.addItem("")
        self.combo_output.addItem("")
        self.horizontalLayout_8.addWidget(self.combo_output)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.text_learning = QtGui.QTextBrowser(Learn)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_learning.sizePolicy().hasHeightForWidth())
        self.text_learning.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.text_learning.setPalette(palette)
        self.text_learning.setObjectName("text_learning")
        self.verticalLayout_2.addWidget(self.text_learning)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)

        self.retranslateUi(Learn)
        self.combo_algorithm.setCurrentIndex(2)
        self.combo_hidden.setCurrentIndex(5)
        self.combo_output.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(Learn)

    def retranslateUi(self, Learn):
        Learn.setWindowTitle(QtGui.QApplication.translate("Learn", "Learning manager", None, QtGui.QApplication.UnicodeUTF8))
        self.button_exp_delete.setText(QtGui.QApplication.translate("Learn", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.button_learn.setText(QtGui.QApplication.translate("Learn", "Learn", None, QtGui.QApplication.UnicodeUTF8))
        self.button_delete.setText(QtGui.QApplication.translate("Learn", "Delete net", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Learn", "Hidden neurons", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Learn", "Desired error", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Learn", "Max epochs", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Learn", "Connection rate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Learn", "Reports frequency", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Learn", "Training algorithm", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_algorithm.setItemText(0, QtGui.QApplication.translate("Learn", "TRAIN_INCREMENTAL", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_algorithm.setItemText(1, QtGui.QApplication.translate("Learn", "TRAIN_BATCH", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_algorithm.setItemText(2, QtGui.QApplication.translate("Learn", "TRAIN_RPROP", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_algorithm.setItemText(3, QtGui.QApplication.translate("Learn", "TRAIN_QUICKPROP", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Learn", "Hidden activation function ", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_hidden.setItemText(0, QtGui.QApplication.translate("Learn", "LINEAR", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_hidden.setItemText(1, QtGui.QApplication.translate("Learn", "THRESHOLD", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_hidden.setItemText(2, QtGui.QApplication.translate("Learn", "THRESHOLD_SYMMETRIC", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_hidden.setItemText(3, QtGui.QApplication.translate("Learn", "SIGMOID", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_hidden.setItemText(4, QtGui.QApplication.translate("Learn", "SIGMOID_STEPWISE", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_hidden.setItemText(5, QtGui.QApplication.translate("Learn", "SIGMOID_SYMMETRIC", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_hidden.setItemText(6, QtGui.QApplication.translate("Learn", "SIGMOID_SYMMETRIC_STEPWISE", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_hidden.setItemText(7, QtGui.QApplication.translate("Learn", "GAUSSIAN", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_hidden.setItemText(8, QtGui.QApplication.translate("Learn", "GAUSSIAN_SYMMETRIC", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_hidden.setItemText(9, QtGui.QApplication.translate("Learn", "GAUSSIAN_STEPWISE", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_hidden.setItemText(10, QtGui.QApplication.translate("Learn", "ELLIOT", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_hidden.setItemText(11, QtGui.QApplication.translate("Learn", "ELLIOT_SYMMETRIC", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_hidden.setItemText(12, QtGui.QApplication.translate("Learn", "LINEAR_PIECE", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_hidden.setItemText(13, QtGui.QApplication.translate("Learn", "LINEAR_PIECE_SYMMETRIC", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_hidden.setItemText(14, QtGui.QApplication.translate("Learn", "SIN_SYMMETRIC", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_hidden.setItemText(15, QtGui.QApplication.translate("Learn", "COS_SYMMETRIC", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Learn", "Output activation function", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_output.setItemText(0, QtGui.QApplication.translate("Learn", "LINEAR", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_output.setItemText(1, QtGui.QApplication.translate("Learn", "THRESHOLD", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_output.setItemText(2, QtGui.QApplication.translate("Learn", "THRESHOLD_SYMMETRIC", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_output.setItemText(3, QtGui.QApplication.translate("Learn", "SIGMOID", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_output.setItemText(4, QtGui.QApplication.translate("Learn", "SIGMOID_STEPWISE", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_output.setItemText(5, QtGui.QApplication.translate("Learn", "SIGMOID_SYMMETRIC", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_output.setItemText(6, QtGui.QApplication.translate("Learn", "SIGMOID_SYMMETRIC_STEPWISE", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_output.setItemText(7, QtGui.QApplication.translate("Learn", "GAUSSIAN", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_output.setItemText(8, QtGui.QApplication.translate("Learn", "GAUSSIAN_SYMMETRIC", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_output.setItemText(9, QtGui.QApplication.translate("Learn", "GAUSSIAN_STEPWISE", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_output.setItemText(10, QtGui.QApplication.translate("Learn", "ELLIOT", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_output.setItemText(11, QtGui.QApplication.translate("Learn", "ELLIOT_SYMMETRIC", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_output.setItemText(12, QtGui.QApplication.translate("Learn", "LINEAR_PIECE", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_output.setItemText(13, QtGui.QApplication.translate("Learn", "LINEAR_PIECE_SYMMETRIC", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_output.setItemText(14, QtGui.QApplication.translate("Learn", "SIN_SYMMETRIC", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_output.setItemText(15, QtGui.QApplication.translate("Learn", "COS_SYMMETRIC", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
