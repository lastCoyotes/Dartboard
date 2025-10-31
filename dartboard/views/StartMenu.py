# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StartMenu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StartMenu(object):
    def setupUi(self, StartMenu):
        if not StartMenu.objectName():
            StartMenu.setObjectName(u"StartMenu")
        StartMenu.resize(676, 618)
        self.centralwidget = QWidget(StartMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"MS Gothic")
        font.setPointSize(28)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.new_match_button = QPushButton(self.centralwidget)
        self.new_match_button.setObjectName(u"new_match_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.new_match_button.sizePolicy().hasHeightForWidth())
        self.new_match_button.setSizePolicy(sizePolicy1)
        self.new_match_button.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.new_match_button, 0, Qt.AlignHCenter)

        self.manage_players_button = QPushButton(self.centralwidget)
        self.manage_players_button.setObjectName(u"manage_players_button")
        sizePolicy1.setHeightForWidth(self.manage_players_button.sizePolicy().hasHeightForWidth())
        self.manage_players_button.setSizePolicy(sizePolicy1)
        self.manage_players_button.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.manage_players_button, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.generate_players_button = QPushButton(self.centralwidget)
        self.generate_players_button.setObjectName(u"generate_players_button")
        sizePolicy1.setHeightForWidth(self.generate_players_button.sizePolicy().hasHeightForWidth())
        self.generate_players_button.setSizePolicy(sizePolicy1)
        self.generate_players_button.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.generate_players_button, 0, Qt.AlignHCenter)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        StartMenu.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(StartMenu)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 676, 21))
        StartMenu.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(StartMenu)
        self.statusbar.setObjectName(u"statusbar")
        StartMenu.setStatusBar(self.statusbar)

        self.retranslateUi(StartMenu)

        QMetaObject.connectSlotsByName(StartMenu)
    # setupUi

    def retranslateUi(self, StartMenu):
        StartMenu.setWindowTitle(QCoreApplication.translate("StartMenu", u"StartMenu", None))
        self.label.setText(QCoreApplication.translate("StartMenu", u"Dart Premier League", None))
        self.new_match_button.setText(QCoreApplication.translate("StartMenu", u"New Game", None))
        self.manage_players_button.setText(QCoreApplication.translate("StartMenu", u"Manage Players", None))
        self.generate_players_button.setText(QCoreApplication.translate("StartMenu", u"Generate Players", None))
    # retranslateUi

