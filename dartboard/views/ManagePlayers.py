# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ManagePlayers.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ManagePlayers(object):
    def setupUi(self, ManagePlayers):
        if not ManagePlayers.objectName():
            ManagePlayers.setObjectName(u"ManagePlayers")
        ManagePlayers.resize(800, 600)
        self.centralwidget = QWidget(ManagePlayers)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(616, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.return_button = QPushButton(self.centralwidget)
        self.return_button.setObjectName(u"return_button")

        self.gridLayout.addWidget(self.return_button, 2, 2, 1, 1)

        self.new_player_button = QPushButton(self.centralwidget)
        self.new_player_button.setObjectName(u"new_player_button")

        self.gridLayout.addWidget(self.new_player_button, 0, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.players_table_widget = QTableWidget(self.centralwidget)
        if (self.players_table_widget.columnCount() < 7):
            self.players_table_widget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.players_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.players_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.players_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.players_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.players_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.players_table_widget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.players_table_widget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.players_table_widget.setObjectName(u"players_table_widget")
        self.players_table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.players_table_widget.setColumnCount(7)
        self.players_table_widget.horizontalHeader().setDefaultSectionSize(112)

        self.gridLayout.addWidget(self.players_table_widget, 1, 0, 1, 3)

        ManagePlayers.setCentralWidget(self.centralwidget)

        self.retranslateUi(ManagePlayers)

        QMetaObject.connectSlotsByName(ManagePlayers)
    # setupUi

    def retranslateUi(self, ManagePlayers):
        ManagePlayers.setWindowTitle(QCoreApplication.translate("ManagePlayers", u"MainWindow", None))
        self.return_button.setText(QCoreApplication.translate("ManagePlayers", u"Back", None))
        self.new_player_button.setText(QCoreApplication.translate("ManagePlayers", u"New Player", None))
        self.label.setText(QCoreApplication.translate("ManagePlayers", u"Manage Players", None))
        ___qtablewidgetitem = self.players_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ManagePlayers", u"Name", None));
        ___qtablewidgetitem1 = self.players_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ManagePlayers", u"League Rank", None));
        ___qtablewidgetitem2 = self.players_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ManagePlayers", u"Avg Season Score", None));
        ___qtablewidgetitem3 = self.players_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ManagePlayers", u"Avg Lifetime Score", None));
        ___qtablewidgetitem4 = self.players_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ManagePlayers", u"Number of 180s", None));
        ___qtablewidgetitem5 = self.players_table_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ManagePlayers", u"# Season Turns", None));
        ___qtablewidgetitem6 = self.players_table_widget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ManagePlayers", u"Remove", None));
    # retranslateUi

