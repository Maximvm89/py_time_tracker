# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tracking_task.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(622, 251)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.software_table = QTableView(self.frame)
        self.software_table.setObjectName(u"software_table")
        self.software_table.setMinimumSize(QSize(171, 173))
        self.software_table.setMaximumSize(QSize(171, 16777215))

        self.verticalLayout.addWidget(self.software_table)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(385, 66))

        self.verticalLayout_2.addWidget(self.label_2)

        self.lcdNumber = QLCDNumber(self.frame_2)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setMinimumSize(QSize(385, 67))
        self.lcdNumber.setMaximumSize(QSize(385, 16777215))
        self.lcdNumber.setLayoutDirection(Qt.LeftToRight)
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setStyleSheet(u"background-color:gray;")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setMode(QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 0.000000000000000)
        self.lcdNumber.setProperty("intValue", 0)

        self.verticalLayout_2.addWidget(self.lcdNumber, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pause_button = QPushButton(self.frame_2)
        self.pause_button.setObjectName(u"pause_button")

        self.horizontalLayout.addWidget(self.pause_button)

        self.stop_button = QPushButton(self.frame_2)
        self.stop_button.setObjectName(u"stop_button")

        self.horizontalLayout.addWidget(self.stop_button)

        self.start_button = QPushButton(self.frame_2)
        self.start_button.setObjectName(u"start_button")

        self.horizontalLayout.addWidget(self.start_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.frame_2)


        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Software detected", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Total Time:", None))
        self.pause_button.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

