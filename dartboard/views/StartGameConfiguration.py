# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StartGameConfiguration.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StartGameConfiguration(object):
    def setupUi(self, StartGameConfiguration):
        if not StartGameConfiguration.objectName():
            StartGameConfiguration.setObjectName(u"StartGameConfiguration")
        StartGameConfiguration.resize(400, 600)
        self.centralwidget = QWidget(StartGameConfiguration)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.player_two_combo_box = QComboBox(self.centralwidget)
        self.player_two_combo_box.setObjectName(u"player_two_combo_box")
        self.player_two_combo_box.setEditable(True)

        self.gridLayout.addWidget(self.player_two_combo_box, 3, 0, 1, 7)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 3)

        self.lifetime_averages_radio_button = QRadioButton(self.centralwidget)
        self.lifetime_averages_radio_button.setObjectName(u"lifetime_averages_radio_button")

        self.gridLayout.addWidget(self.lifetime_averages_radio_button, 17, 5, 1, 2)

        self.official_names_line_edit = QLineEdit(self.centralwidget)
        self.official_names_line_edit.setObjectName(u"official_names_line_edit")

        self.gridLayout.addWidget(self.official_names_line_edit, 5, 0, 1, 7)

        self.triples_doubles_radio_button = QRadioButton(self.centralwidget)
        self.triples_doubles_radio_button.setObjectName(u"triples_doubles_radio_button")

        self.gridLayout.addWidget(self.triples_doubles_radio_button, 17, 3, 1, 2)

        self.date_edit = QDateEdit(self.centralwidget)
        self.date_edit.setObjectName(u"date_edit")

        self.gridLayout.addWidget(self.date_edit, 9, 0, 1, 7)

        self.lifetime_scores_radio_button = QRadioButton(self.centralwidget)
        self.lifetime_scores_radio_button.setObjectName(u"lifetime_scores_radio_button")
        self.lifetime_scores_radio_button.setChecked(True)

        self.gridLayout.addWidget(self.lifetime_scores_radio_button, 18, 5, 1, 2)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 15, 0, 1, 7, Qt.AlignHCenter)

        self.leg_value_501_radio_button = QRadioButton(self.centralwidget)
        self.leg_value_501_radio_button.setObjectName(u"leg_value_501_radio_button")

        self.gridLayout.addWidget(self.leg_value_501_radio_button, 13, 4, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_6, 12, 1, 1, 5)

        self.match_highest_out_radio_button = QRadioButton(self.centralwidget)
        self.match_highest_out_radio_button.setObjectName(u"match_highest_out_radio_button")

        self.gridLayout.addWidget(self.match_highest_out_radio_button, 19, 0, 1, 3)

        self.start_game_button = QPushButton(self.centralwidget)
        self.start_game_button.setObjectName(u"start_game_button")

        self.gridLayout.addWidget(self.start_game_button, 21, 4, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 20, 4, 1, 1)

        self.number_of_sets_spin_box = QSpinBox(self.centralwidget)
        self.number_of_sets_spin_box.setObjectName(u"number_of_sets_spin_box")

        self.gridLayout.addWidget(self.number_of_sets_spin_box, 11, 6, 1, 1)

        self.match_score_stats_radio_button = QRadioButton(self.centralwidget)
        self.match_score_stats_radio_button.setObjectName(u"match_score_stats_radio_button")

        self.gridLayout.addWidget(self.match_score_stats_radio_button, 18, 0, 1, 3)

        self.number_of_legs_spin_box = QSpinBox(self.centralwidget)
        self.number_of_legs_spin_box.setObjectName(u"number_of_legs_spin_box")

        self.gridLayout.addWidget(self.number_of_legs_spin_box, 11, 0, 1, 1)

        self.player_last_win_radio_button = QRadioButton(self.centralwidget)
        self.player_last_win_radio_button.setObjectName(u"player_last_win_radio_button")

        self.gridLayout.addWidget(self.player_last_win_radio_button, 19, 3, 1, 2)

        self.player_one_combo_box = QComboBox(self.centralwidget)
        self.player_one_combo_box.setObjectName(u"player_one_combo_box")
        self.player_one_combo_box.setEditable(True)

        self.gridLayout.addWidget(self.player_one_combo_box, 1, 0, 1, 7)

        self.player_rank_radio_button = QRadioButton(self.centralwidget)
        self.player_rank_radio_button.setObjectName(u"player_rank_radio_button")

        self.gridLayout.addWidget(self.player_rank_radio_button, 18, 3, 1, 2)

        self.leg_value_301_radio_button = QRadioButton(self.centralwidget)
        self.leg_value_301_radio_button.setObjectName(u"leg_value_301_radio_button")

        self.gridLayout.addWidget(self.leg_value_301_radio_button, 13, 5, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.match_averages_radio_button = QRadioButton(self.centralwidget)
        self.match_averages_radio_button.setObjectName(u"match_averages_radio_button")

        self.gridLayout.addWidget(self.match_averages_radio_button, 17, 0, 1, 3)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_5, 10, 6, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 2)

        self.location_line_edit = QLineEdit(self.centralwidget)
        self.location_line_edit.setObjectName(u"location_line_edit")

        self.gridLayout.addWidget(self.location_line_edit, 7, 0, 1, 7)

        self.leg_value_801_radio_button = QRadioButton(self.centralwidget)
        self.leg_value_801_radio_button.setObjectName(u"leg_value_801_radio_button")

        self.gridLayout.addWidget(self.leg_value_801_radio_button, 13, 2, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 14, 0, 1, 1)

        StartGameConfiguration.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(StartGameConfiguration)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 21))
        StartGameConfiguration.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(StartGameConfiguration)
        self.statusbar.setObjectName(u"statusbar")
        StartGameConfiguration.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.location_line_edit, self.date_edit)
        QWidget.setTabOrder(self.date_edit, self.number_of_legs_spin_box)
        QWidget.setTabOrder(self.number_of_legs_spin_box, self.number_of_sets_spin_box)
        QWidget.setTabOrder(self.number_of_sets_spin_box, self.leg_value_801_radio_button)
        QWidget.setTabOrder(self.leg_value_801_radio_button, self.leg_value_501_radio_button)

        self.retranslateUi(StartGameConfiguration)

        QMetaObject.connectSlotsByName(StartGameConfiguration)
    # setupUi

    def retranslateUi(self, StartGameConfiguration):
        StartGameConfiguration.setWindowTitle(QCoreApplication.translate("StartGameConfiguration", u"Start Game Configuration", None))
        self.label_9.setText(QCoreApplication.translate("StartGameConfiguration", u"Official Names", None))
        self.lifetime_averages_radio_button.setText(QCoreApplication.translate("StartGameConfiguration", u"Lifetime Averages", None))
        self.triples_doubles_radio_button.setText(QCoreApplication.translate("StartGameConfiguration", u"Triples Doubles", None))
        self.lifetime_scores_radio_button.setText(QCoreApplication.translate("StartGameConfiguration", u"Lifetime Scores", None))
        self.label_7.setText(QCoreApplication.translate("StartGameConfiguration", u"Starting Stats Display", None))
        self.leg_value_501_radio_button.setText(QCoreApplication.translate("StartGameConfiguration", u"501", None))
        self.label_6.setText(QCoreApplication.translate("StartGameConfiguration", u"Scoring Leg Value", None))
        self.match_highest_out_radio_button.setText(QCoreApplication.translate("StartGameConfiguration", u"Match Highest Out", None))
        self.start_game_button.setText(QCoreApplication.translate("StartGameConfiguration", u"Start Game", None))
        self.label_2.setText(QCoreApplication.translate("StartGameConfiguration", u"Player 2 Name", None))
        self.match_score_stats_radio_button.setText(QCoreApplication.translate("StartGameConfiguration", u"Match Score Stats", None))
        self.player_last_win_radio_button.setText(QCoreApplication.translate("StartGameConfiguration", u"Player Last Win", None))
        self.player_rank_radio_button.setText(QCoreApplication.translate("StartGameConfiguration", u"Player Rank", None))
        self.leg_value_301_radio_button.setText(QCoreApplication.translate("StartGameConfiguration", u"301", None))
        self.label_8.setText(QCoreApplication.translate("StartGameConfiguration", u"Date", None))
        self.label.setText(QCoreApplication.translate("StartGameConfiguration", u"Player 1 Name", None))
        self.match_averages_radio_button.setText(QCoreApplication.translate("StartGameConfiguration", u"Match Averages", None))
        self.label_5.setText(QCoreApplication.translate("StartGameConfiguration", u"Number of Matches", None))
        self.label_3.setText(QCoreApplication.translate("StartGameConfiguration", u"Location", None))
        self.leg_value_801_radio_button.setText(QCoreApplication.translate("StartGameConfiguration", u"801", None))
        self.label_4.setText(QCoreApplication.translate("StartGameConfiguration", u"Number of Legs", None))
    # retranslateUi

