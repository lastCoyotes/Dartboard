# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewPlayer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NewPlayer(object):
    def setupUi(self, NewPlayer):
        if not NewPlayer.objectName():
            NewPlayer.setObjectName(u"NewPlayer")
        NewPlayer.resize(312, 232)
        self.centralwidget = QWidget(NewPlayer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.reject_button = QPushButton(self.centralwidget)
        self.reject_button.setObjectName(u"reject_button")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reject_button.sizePolicy().hasHeightForWidth())
        self.reject_button.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.reject_button, 2, 4, 1, 1)

        self.accept_button = QPushButton(self.centralwidget)
        self.accept_button.setObjectName(u"accept_button")
        sizePolicy.setHeightForWidth(self.accept_button.sizePolicy().hasHeightForWidth())
        self.accept_button.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.accept_button, 2, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.first_name_line_edit = QLineEdit(self.centralwidget)
        self.first_name_line_edit.setObjectName(u"first_name_line_edit")

        self.gridLayout.addWidget(self.first_name_line_edit, 0, 1, 1, 4)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.last_name_line_edit = QLineEdit(self.centralwidget)
        self.last_name_line_edit.setObjectName(u"last_name_line_edit")

        self.gridLayout.addWidget(self.last_name_line_edit, 1, 1, 1, 4)

        NewPlayer.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(NewPlayer)
        self.statusbar.setObjectName(u"statusbar")
        NewPlayer.setStatusBar(self.statusbar)

        self.retranslateUi(NewPlayer)

        QMetaObject.connectSlotsByName(NewPlayer)
    # setupUi

    def retranslateUi(self, NewPlayer):
        NewPlayer.setWindowTitle(QCoreApplication.translate("NewPlayer", u"Add New Player", None))
        self.reject_button.setText(QCoreApplication.translate("NewPlayer", u"Cancel", None))
        self.accept_button.setText(QCoreApplication.translate("NewPlayer", u"Ok", None))
        self.label.setText(QCoreApplication.translate("NewPlayer", u"First Name:", None))
        self.label_2.setText(QCoreApplication.translate("NewPlayer", u"Last Name:", None))
    # retranslateUi

