# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Scoreboard.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from DartboardViewer import DartboardViewer


class Ui_Scoreboard(object):
    def setupUi(self, Scoreboard):
        if not Scoreboard.objectName():
            Scoreboard.setObjectName(u"Scoreboard")
        Scoreboard.resize(1766, 1173)
        self.centralwidget = QWidget(Scoreboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.graphicsView = DartboardViewer(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 3, 2, 1, 3)

        self.current_score = QLabel(self.centralwidget)
        self.current_score.setObjectName(u"current_score")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_score.sizePolicy().hasHeightForWidth())
        self.current_score.setSizePolicy(sizePolicy)
        self.current_score.setMinimumSize(QSize(102, 75))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.current_score.setFont(font)
        self.current_score.setStyleSheet(u"")
        self.current_score.setFrameShape(QFrame.StyledPanel)
        self.current_score.setFrameShadow(QFrame.Plain)
        self.current_score.setLineWidth(5)
        self.current_score.setMidLineWidth(1)
        self.current_score.setTextFormat(Qt.AutoText)
        self.current_score.setScaledContents(True)
        self.current_score.setAlignment(Qt.AlignCenter)
        self.current_score.setWordWrap(False)

        self.gridLayout.addWidget(self.current_score, 4, 3, 1, 1)

        self.player_one_win_label = QLabel(self.centralwidget)
        self.player_one_win_label.setObjectName(u"player_one_win_label")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(16)
        self.player_one_win_label.setFont(font1)

        self.gridLayout.addWidget(self.player_one_win_label, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.player_1_stats = QLabel(self.centralwidget)
        self.player_1_stats.setObjectName(u"player_1_stats")

        self.gridLayout.addWidget(self.player_1_stats, 4, 0, 1, 1)

        self.player_1_score = QLCDNumber(self.centralwidget)
        self.player_1_score.setObjectName(u"player_1_score")
        self.player_1_score.setMaximumSize(QSize(90, 30))
        font2 = QFont()
        font2.setPointSize(27)
        font2.setBold(True)
        font2.setWeight(75)
        self.player_1_score.setFont(font2)
        self.player_1_score.setFrameShape(QFrame.StyledPanel)
        self.player_1_score.setFrameShadow(QFrame.Plain)
        self.player_1_score.setSmallDecimalPoint(False)
        self.player_1_score.setDigitCount(3)
        self.player_1_score.setMode(QLCDNumber.Dec)
        self.player_1_score.setSegmentStyle(QLCDNumber.Flat)
        self.player_1_score.setProperty("value", 501.000000000000000)

        self.gridLayout.addWidget(self.player_1_score, 4, 2, 1, 1)

        self.player_2_stats = QLabel(self.centralwidget)
        self.player_2_stats.setObjectName(u"player_2_stats")

        self.gridLayout.addWidget(self.player_2_stats, 4, 5, 1, 1)

        self.player_1_name = QLabel(self.centralwidget)
        self.player_1_name.setObjectName(u"player_1_name")
        sizePolicy.setHeightForWidth(self.player_1_name.sizePolicy().hasHeightForWidth())
        self.player_1_name.setSizePolicy(sizePolicy)
        self.player_1_name.setMaximumSize(QSize(200, 30))
        self.player_1_name.setFont(font)
        self.player_1_name.setLayoutDirection(Qt.LeftToRight)
        self.player_1_name.setStyleSheet(u"")
        self.player_1_name.setFrameShape(QFrame.StyledPanel)
        self.player_1_name.setFrameShadow(QFrame.Plain)
        self.player_1_name.setLineWidth(5)
        self.player_1_name.setMidLineWidth(1)
        self.player_1_name.setTextFormat(Qt.AutoText)
        self.player_1_name.setScaledContents(True)
        self.player_1_name.setAlignment(Qt.AlignCenter)
        self.player_1_name.setWordWrap(False)

        self.gridLayout.addWidget(self.player_1_name, 2, 0, 1, 1, Qt.AlignHCenter)

        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setMinimumSize(QSize(380, 75))
        self.title.setFont(font)
        self.title.setStyleSheet(u"")
        self.title.setFrameShape(QFrame.StyledPanel)
        self.title.setFrameShadow(QFrame.Plain)
        self.title.setLineWidth(5)
        self.title.setMidLineWidth(1)
        self.title.setTextFormat(Qt.AutoText)
        self.title.setScaledContents(True)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setWordWrap(False)

        self.gridLayout.addWidget(self.title, 2, 3, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.Player2DartsTable = QTableWidget(self.centralwidget)
        if (self.Player2DartsTable.columnCount() < 4):
            self.Player2DartsTable.setColumnCount(4)
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.Player2DartsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        font4.setStyleStrategy(QFont.PreferAntialias)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        self.Player2DartsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        self.Player2DartsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        self.Player2DartsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.Player2DartsTable.setObjectName(u"Player2DartsTable")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Player2DartsTable.sizePolicy().hasHeightForWidth())
        self.Player2DartsTable.setSizePolicy(sizePolicy1)
        self.Player2DartsTable.setMinimumSize(QSize(400, 200))
        self.Player2DartsTable.setMaximumSize(QSize(400, 400))
        self.Player2DartsTable.setLayoutDirection(Qt.LeftToRight)
        self.Player2DartsTable.setStyleSheet(u"gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Player2DartsTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Player2DartsTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Player2DartsTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Player2DartsTable.setAlternatingRowColors(True)
        self.Player2DartsTable.setShowGrid(True)
        self.Player2DartsTable.setGridStyle(Qt.SolidLine)
        self.Player2DartsTable.setRowCount(0)
        self.Player2DartsTable.horizontalHeader().setVisible(True)
        self.Player2DartsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.Player2DartsTable.horizontalHeader().setMinimumSectionSize(100)
        self.Player2DartsTable.horizontalHeader().setDefaultSectionSize(100)
        self.Player2DartsTable.horizontalHeader().setHighlightSections(True)
        self.Player2DartsTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.Player2DartsTable.horizontalHeader().setStretchLastSection(False)
        self.Player2DartsTable.verticalHeader().setVisible(False)
        self.Player2DartsTable.verticalHeader().setCascadingSectionResizes(True)
        self.Player2DartsTable.verticalHeader().setMinimumSectionSize(23)
        self.Player2DartsTable.verticalHeader().setDefaultSectionSize(30)
        self.Player2DartsTable.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_3.addWidget(self.Player2DartsTable)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(17)
        self.label.setFont(font5)

        self.verticalLayout_3.addWidget(self.label)

        self.player_two_checkouts_label = QLabel(self.centralwidget)
        self.player_two_checkouts_label.setObjectName(u"player_two_checkouts_label")
        font6 = QFont()
        font6.setPointSize(13)
        self.player_two_checkouts_label.setFont(font6)

        self.verticalLayout_3.addWidget(self.player_two_checkouts_label)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.fewest_darts_player_two_label = QLabel(self.centralwidget)
        self.fewest_darts_player_two_label.setObjectName(u"fewest_darts_player_two_label")
        self.fewest_darts_player_two_label.setFont(font5)

        self.verticalLayout_3.addWidget(self.fewest_darts_player_two_label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.player_two_additional_stats = QLabel(self.centralwidget)
        self.player_two_additional_stats.setObjectName(u"player_two_additional_stats")
        self.player_two_additional_stats.setEnabled(True)
        self.player_two_additional_stats.setFont(font6)
        self.player_two_additional_stats.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.player_two_additional_stats)


        self.gridLayout.addLayout(self.verticalLayout_3, 3, 5, 1, 1)

        self.player_2_score = QLCDNumber(self.centralwidget)
        self.player_2_score.setObjectName(u"player_2_score")
        self.player_2_score.setMaximumSize(QSize(60, 30))
        font7 = QFont()
        font7.setPointSize(9)
        self.player_2_score.setFont(font7)
        self.player_2_score.setFrameShape(QFrame.StyledPanel)
        self.player_2_score.setFrameShadow(QFrame.Plain)
        self.player_2_score.setSmallDecimalPoint(False)
        self.player_2_score.setDigitCount(3)
        self.player_2_score.setMode(QLCDNumber.Dec)
        self.player_2_score.setSegmentStyle(QLCDNumber.Flat)
        self.player_2_score.setProperty("value", 501.000000000000000)

        self.gridLayout.addWidget(self.player_2_score, 4, 4, 1, 1)

        self.player_2_name = QLabel(self.centralwidget)
        self.player_2_name.setObjectName(u"player_2_name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.player_2_name.sizePolicy().hasHeightForWidth())
        self.player_2_name.setSizePolicy(sizePolicy2)
        self.player_2_name.setMaximumSize(QSize(200, 30))
        self.player_2_name.setFont(font)
        self.player_2_name.setLayoutDirection(Qt.LeftToRight)
        self.player_2_name.setStyleSheet(u"")
        self.player_2_name.setFrameShape(QFrame.StyledPanel)
        self.player_2_name.setFrameShadow(QFrame.Plain)
        self.player_2_name.setLineWidth(5)
        self.player_2_name.setMidLineWidth(1)
        self.player_2_name.setTextFormat(Qt.AutoText)
        self.player_2_name.setScaledContents(True)
        self.player_2_name.setAlignment(Qt.AlignCenter)
        self.player_2_name.setWordWrap(False)

        self.gridLayout.addWidget(self.player_2_name, 2, 5, 1, 1, Qt.AlignHCenter)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.Player1DartsTable = QTableWidget(self.centralwidget)
        if (self.Player1DartsTable.columnCount() < 4):
            self.Player1DartsTable.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.Player1DartsTable.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        self.Player1DartsTable.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3);
        self.Player1DartsTable.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font3);
        self.Player1DartsTable.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.Player1DartsTable.setObjectName(u"Player1DartsTable")
        self.Player1DartsTable.setMinimumSize(QSize(400, 200))
        self.Player1DartsTable.setMaximumSize(QSize(400, 400))
        self.Player1DartsTable.setStyleSheet(u"gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Player1DartsTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Player1DartsTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Player1DartsTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Player1DartsTable.setAlternatingRowColors(True)
        self.Player1DartsTable.setShowGrid(True)
        self.Player1DartsTable.setGridStyle(Qt.SolidLine)
        self.Player1DartsTable.setRowCount(0)
        self.Player1DartsTable.setColumnCount(4)
        self.Player1DartsTable.horizontalHeader().setVisible(True)
        self.Player1DartsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.Player1DartsTable.horizontalHeader().setMinimumSectionSize(100)
        self.Player1DartsTable.horizontalHeader().setDefaultSectionSize(100)
        self.Player1DartsTable.horizontalHeader().setHighlightSections(True)
        self.Player1DartsTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.Player1DartsTable.horizontalHeader().setStretchLastSection(False)
        self.Player1DartsTable.verticalHeader().setVisible(False)
        self.Player1DartsTable.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_2.addWidget(self.Player1DartsTable)

        self.player_one_label = QLabel(self.centralwidget)
        self.player_one_label.setObjectName(u"player_one_label")
        self.player_one_label.setFont(font5)

        self.verticalLayout_2.addWidget(self.player_one_label)

        self.player_one_checkouts_label = QLabel(self.centralwidget)
        self.player_one_checkouts_label.setObjectName(u"player_one_checkouts_label")
        self.player_one_checkouts_label.setFont(font6)

        self.verticalLayout_2.addWidget(self.player_one_checkouts_label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.fewest_darts_player_one_label = QLabel(self.centralwidget)
        self.fewest_darts_player_one_label.setObjectName(u"fewest_darts_player_one_label")
        self.fewest_darts_player_one_label.setFont(font5)

        self.verticalLayout_2.addWidget(self.fewest_darts_player_one_label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.player_one_additional_stats = QLabel(self.centralwidget)
        self.player_one_additional_stats.setObjectName(u"player_one_additional_stats")
        self.player_one_additional_stats.setEnabled(True)
        self.player_one_additional_stats.setFont(font6)
        self.player_one_additional_stats.setTextFormat(Qt.AutoText)
        self.player_one_additional_stats.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.player_one_additional_stats)


        self.gridLayout.addLayout(self.verticalLayout_2, 3, 0, 1, 1)

        self.player_two_win_label = QLabel(self.centralwidget)
        self.player_two_win_label.setObjectName(u"player_two_win_label")
        self.player_two_win_label.setFont(font1)

        self.gridLayout.addWidget(self.player_two_win_label, 1, 5, 1, 1, Qt.AlignHCenter)

        Scoreboard.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Scoreboard)
        self.statusbar.setObjectName(u"statusbar")
        Scoreboard.setStatusBar(self.statusbar)

        self.retranslateUi(Scoreboard)

        QMetaObject.connectSlotsByName(Scoreboard)
    # setupUi

    def retranslateUi(self, Scoreboard):
        Scoreboard.setWindowTitle(QCoreApplication.translate("Scoreboard", u"MainWindow", None))
        self.current_score.setText(QCoreApplication.translate("Scoreboard", u"Current Score", None))
        self.player_one_win_label.setText(QCoreApplication.translate("Scoreboard", u"WINNER", None))
        self.player_1_stats.setText("")
        self.player_2_stats.setText("")
        self.player_1_name.setText(QCoreApplication.translate("Scoreboard", u"<Player 1 Name>", None))
        self.title.setText(QCoreApplication.translate("Scoreboard", u"English Premier Dart League", None))
        ___qtablewidgetitem = self.Player2DartsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Scoreboard", u"Score", None));
        ___qtablewidgetitem1 = self.Player2DartsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Scoreboard", u"Bounce Out", None));
        ___qtablewidgetitem2 = self.Player2DartsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Scoreboard", u"Knock Out", None));
        ___qtablewidgetitem3 = self.Player2DartsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Scoreboard", u"Foul", None));
        self.label.setText(QCoreApplication.translate("Scoreboard", u"Checkouts", None))
        self.player_two_checkouts_label.setText(QCoreApplication.translate("Scoreboard", u"TextLabel", None))
        self.fewest_darts_player_two_label.setText(QCoreApplication.translate("Scoreboard", u"<html><head/><body><p><span style=\" color:#00ff00;\">On Track For Perfect Leg</span></p></body></html>", None))
        self.player_two_additional_stats.setText(QCoreApplication.translate("Scoreboard", u"TextLabel", None))
        self.player_2_name.setText(QCoreApplication.translate("Scoreboard", u"<Player 2 Name>", None))
        ___qtablewidgetitem4 = self.Player1DartsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Scoreboard", u"Score", None));
        ___qtablewidgetitem5 = self.Player1DartsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Scoreboard", u"Bounce Out", None));
        ___qtablewidgetitem6 = self.Player1DartsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Scoreboard", u"Knock Out", None));
        ___qtablewidgetitem7 = self.Player1DartsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Scoreboard", u"Foul", None));
        self.player_one_label.setText(QCoreApplication.translate("Scoreboard", u"Checkouts", None))
        self.player_one_checkouts_label.setText(QCoreApplication.translate("Scoreboard", u"TextLabel", None))
        self.fewest_darts_player_one_label.setText(QCoreApplication.translate("Scoreboard", u"<html><head/><body><p><span style=\" color:#00ff00;\">On Track For Perfect Leg</span></p></body></html>", None))
        self.player_one_additional_stats.setText(QCoreApplication.translate("Scoreboard", u"TextLabel", None))
        self.player_two_win_label.setText(QCoreApplication.translate("Scoreboard", u"WINNER", None))
    # retranslateUi

