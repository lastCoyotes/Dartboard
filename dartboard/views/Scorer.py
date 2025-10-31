# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Scorer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from DartboardView import DartboardView


class Ui_Scorer(object):
    def setupUi(self, Scorer):
        if not Scorer.objectName():
            Scorer.setObjectName(u"Scorer")
        Scorer.resize(723, 527)
        self.actionMatch_Averages = QAction(Scorer)
        self.actionMatch_Averages.setObjectName(u"actionMatch_Averages")
        self.actionMatch_Score_Stats = QAction(Scorer)
        self.actionMatch_Score_Stats.setObjectName(u"actionMatch_Score_Stats")
        self.actionMatch_Highest_Out = QAction(Scorer)
        self.actionMatch_Highest_Out.setObjectName(u"actionMatch_Highest_Out")
        self.action_Match_Statistics = QAction(Scorer)
        self.action_Match_Statistics.setObjectName(u"action_Match_Statistics")
        self.match_averages = QAction(Scorer)
        self.match_averages.setObjectName(u"match_averages")
        self.match_score_stats = QAction(Scorer)
        self.match_score_stats.setObjectName(u"match_score_stats")
        self.match_highest_out = QAction(Scorer)
        self.match_highest_out.setObjectName(u"match_highest_out")
        self.match_doubles_triples = QAction(Scorer)
        self.match_doubles_triples.setObjectName(u"match_doubles_triples")
        self.player_ranks = QAction(Scorer)
        self.player_ranks.setObjectName(u"player_ranks")
        self.player_last_win = QAction(Scorer)
        self.player_last_win.setObjectName(u"player_last_win")
        self.player_averages = QAction(Scorer)
        self.player_averages.setObjectName(u"player_averages")
        self.player_score_stats = QAction(Scorer)
        self.player_score_stats.setObjectName(u"player_score_stats")
        self.centralwidget = QWidget(Scorer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 2, Qt.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 5, 2, 1, 3)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.Player1Tab = QWidget()
        self.Player1Tab.setObjectName(u"Player1Tab")
        self.gridLayout_2 = QGridLayout(self.Player1Tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.Player1Tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 3, 1, 1)

        self.player_1_legs = QLabel(self.Player1Tab)
        self.player_1_legs.setObjectName(u"player_1_legs")

        self.gridLayout_2.addWidget(self.player_1_legs, 0, 4, 1, 1)

        self.label_6 = QLabel(self.Player1Tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 5, 1, 1)

        self.player_1_score = QLabel(self.Player1Tab)
        self.player_1_score.setObjectName(u"player_1_score")

        self.gridLayout_2.addWidget(self.player_1_score, 0, 2, 1, 1)

        self.label_3 = QLabel(self.Player1Tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1, Qt.AlignRight)

        self.player_1_matches = QLabel(self.Player1Tab)
        self.player_1_matches.setObjectName(u"player_1_matches")

        self.gridLayout_2.addWidget(self.player_1_matches, 0, 6, 1, 1)

        self.Player1DartsTable = QTableWidget(self.Player1Tab)
        if (self.Player1DartsTable.columnCount() < 5):
            self.Player1DartsTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.Player1DartsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Player1DartsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Player1DartsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Player1DartsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.Player1DartsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.Player1DartsTable.setObjectName(u"Player1DartsTable")
        self.Player1DartsTable.setColumnCount(5)
        self.Player1DartsTable.horizontalHeader().setDefaultSectionSize(74)
        self.Player1DartsTable.horizontalHeader().setStretchLastSection(False)
        self.Player1DartsTable.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.Player1DartsTable, 3, 1, 1, 6)

        self.tabWidget.addTab(self.Player1Tab, "")
        self.Player2Tab = QWidget()
        self.Player2Tab.setObjectName(u"Player2Tab")
        self.gridLayout_3 = QGridLayout(self.Player2Tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.player_2_legs = QLabel(self.Player2Tab)
        self.player_2_legs.setObjectName(u"player_2_legs")

        self.gridLayout_3.addWidget(self.player_2_legs, 1, 3, 1, 1)

        self.label_13 = QLabel(self.Player2Tab)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 1, 4, 1, 1)

        self.label_9 = QLabel(self.Player2Tab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)

        self.player_2_score = QLabel(self.Player2Tab)
        self.player_2_score.setObjectName(u"player_2_score")

        self.gridLayout_3.addWidget(self.player_2_score, 1, 1, 1, 1)

        self.label_11 = QLabel(self.Player2Tab)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 1, 2, 1, 1)

        self.player_2_matches = QLabel(self.Player2Tab)
        self.player_2_matches.setObjectName(u"player_2_matches")

        self.gridLayout_3.addWidget(self.player_2_matches, 1, 5, 1, 1)

        self.Player2DartsTable = QTableWidget(self.Player2Tab)
        if (self.Player2DartsTable.columnCount() < 5):
            self.Player2DartsTable.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Player2DartsTable.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.Player2DartsTable.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.Player2DartsTable.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.Player2DartsTable.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.Player2DartsTable.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.Player2DartsTable.setObjectName(u"Player2DartsTable")
        self.Player2DartsTable.setColumnCount(5)
        self.Player2DartsTable.horizontalHeader().setDefaultSectionSize(74)
        self.Player2DartsTable.horizontalHeader().setStretchLastSection(False)
        self.Player2DartsTable.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.Player2DartsTable, 4, 0, 1, 6)

        self.tabWidget.addTab(self.Player2Tab, "")

        self.gridLayout.addWidget(self.tabWidget, 4, 1, 1, 5)

        self.LegNumberLabel = QLabel(self.centralwidget)
        self.LegNumberLabel.setObjectName(u"LegNumberLabel")

        self.gridLayout.addWidget(self.LegNumberLabel, 2, 1, 1, 2, Qt.AlignHCenter)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 2, Qt.AlignHCenter)

        self.graphicsView = DartboardView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(300, 300))

        self.gridLayout.addWidget(self.graphicsView, 0, 0, 6, 1)

        self.SetNumberLabel = QLabel(self.centralwidget)
        self.SetNumberLabel.setObjectName(u"SetNumberLabel")

        self.gridLayout.addWidget(self.SetNumberLabel, 2, 4, 1, 2, Qt.AlignHCenter)

        self.commit_turn_button = QPushButton(self.centralwidget)
        self.commit_turn_button.setObjectName(u"commit_turn_button")

        self.gridLayout.addWidget(self.commit_turn_button, 5, 1, 1, 1)

        self.EndMatchButton = QPushButton(self.centralwidget)
        self.EndMatchButton.setObjectName(u"EndMatchButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.EndMatchButton.sizePolicy().hasHeightForWidth())
        self.EndMatchButton.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.EndMatchButton, 5, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(215, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 3, 1, 1)

        Scorer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Scorer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 723, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        Scorer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Scorer)
        self.statusbar.setObjectName(u"statusbar")
        Scorer.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.match_averages)
        self.menu.addAction(self.match_score_stats)
        self.menu.addAction(self.match_highest_out)
        self.menu.addAction(self.match_doubles_triples)
        self.menu.addSeparator()
        self.menu.addAction(self.player_ranks)
        self.menu.addAction(self.player_last_win)
        self.menu.addAction(self.player_averages)
        self.menu.addAction(self.player_score_stats)

        self.retranslateUi(Scorer)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Scorer)
    # setupUi

    def retranslateUi(self, Scorer):
        Scorer.setWindowTitle(QCoreApplication.translate("Scorer", u"MainWindow", None))
        self.actionMatch_Averages.setText(QCoreApplication.translate("Scorer", u"Match Averages", None))
        self.actionMatch_Score_Stats.setText(QCoreApplication.translate("Scorer", u"Match Score Stats", None))
        self.actionMatch_Highest_Out.setText(QCoreApplication.translate("Scorer", u"Match Highest Out", None))
        self.action_Match_Statistics.setText(QCoreApplication.translate("Scorer", u"-- Match Statistics --", None))
        self.match_averages.setText(QCoreApplication.translate("Scorer", u"Match Averages", None))
        self.match_score_stats.setText(QCoreApplication.translate("Scorer", u"Match Score Stats", None))
        self.match_highest_out.setText(QCoreApplication.translate("Scorer", u"Match Highest Out", None))
        self.match_doubles_triples.setText(QCoreApplication.translate("Scorer", u"Match Doubles/Triples", None))
        self.player_ranks.setText(QCoreApplication.translate("Scorer", u"Player Ranks", None))
        self.player_last_win.setText(QCoreApplication.translate("Scorer", u"Player Last Win", None))
        self.player_averages.setText(QCoreApplication.translate("Scorer", u"Player Averages", None))
        self.player_score_stats.setText(QCoreApplication.translate("Scorer", u"Player Score Stats", None))
        self.label.setText(QCoreApplication.translate("Scorer", u"Current Leg", None))
        self.label_5.setText(QCoreApplication.translate("Scorer", u"Legs Won:", None))
        self.player_1_legs.setText(QCoreApplication.translate("Scorer", u"0", None))
        self.label_6.setText(QCoreApplication.translate("Scorer", u"Matches Won:", None))
        self.player_1_score.setText(QCoreApplication.translate("Scorer", u"0", None))
        self.label_3.setText(QCoreApplication.translate("Scorer", u"Remaining Score:", None))
        self.player_1_matches.setText(QCoreApplication.translate("Scorer", u"0", None))
        ___qtablewidgetitem = self.Player1DartsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Scorer", u"Score", None));
        ___qtablewidgetitem1 = self.Player1DartsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Scorer", u"Bounce Out", None));
        ___qtablewidgetitem2 = self.Player1DartsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Scorer", u"Knock Out", None));
        ___qtablewidgetitem3 = self.Player1DartsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Scorer", u"Foul", None));
        ___qtablewidgetitem4 = self.Player1DartsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Scorer", u"Remove", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Player1Tab), QCoreApplication.translate("Scorer", u"Player 1", None))
        self.player_2_legs.setText(QCoreApplication.translate("Scorer", u"0", None))
        self.label_13.setText(QCoreApplication.translate("Scorer", u"Matches Won:", None))
        self.label_9.setText(QCoreApplication.translate("Scorer", u"Remaining Score:", None))
        self.player_2_score.setText(QCoreApplication.translate("Scorer", u"0", None))
        self.label_11.setText(QCoreApplication.translate("Scorer", u"Legs Won:", None))
        self.player_2_matches.setText(QCoreApplication.translate("Scorer", u"0", None))
        ___qtablewidgetitem5 = self.Player2DartsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Scorer", u"Score", None));
        ___qtablewidgetitem6 = self.Player2DartsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Scorer", u"Bounce Out", None));
        ___qtablewidgetitem7 = self.Player2DartsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Scorer", u"Knock Out", None));
        ___qtablewidgetitem8 = self.Player2DartsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Scorer", u"Foul", None));
        ___qtablewidgetitem9 = self.Player2DartsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Scorer", u"Remove", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Player2Tab), QCoreApplication.translate("Scorer", u"Player 2", None))
        self.LegNumberLabel.setText(QCoreApplication.translate("Scorer", u"4/14", None))
        self.label_2.setText(QCoreApplication.translate("Scorer", u"Current Match", None))
        self.SetNumberLabel.setText(QCoreApplication.translate("Scorer", u"2/4", None))
        self.commit_turn_button.setText(QCoreApplication.translate("Scorer", u"Commit Turn", None))
        self.EndMatchButton.setText(QCoreApplication.translate("Scorer", u"End Game", None))
        self.menu.setTitle(QCoreApplication.translate("Scorer", u"Scoreboard View", None))
    # retranslateUi

