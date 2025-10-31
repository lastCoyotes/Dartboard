from views.StartGameConfiguration import Ui_StartGameConfiguration
from PySide2.QtWidgets import QApplication, QMainWindow, QCompleter, QButtonGroup
from PySide2.QtCore import QDate
from backend.dartboard_api import search_players, get_player_by_full_name, create_match
import sys

class StartGameConfigurationWindow(QMainWindow):
    def __init__(self, hub):
        super(StartGameConfigurationWindow, self).__init__()

        self.hub = hub

        self.ui = Ui_StartGameConfiguration()
        self.ui.setupUi(self)

        self.ui.start_game_button.clicked.connect(self.start_game)

        self.populate_player_names("")
        
        self.enter_start_values()
        self.ui.date_edit.setDate(QDate.currentDate())
        self.scoring_leg_values_group = QButtonGroup()
        self.scoring_leg_values_group.addButton(self.ui.leg_value_801_radio_button)
        self.scoring_leg_values_group.addButton(self.ui.leg_value_501_radio_button)
        self.scoring_leg_values_group.addButton(self.ui.leg_value_301_radio_button)

        self.statistics_group = QButtonGroup()
        
        self.statistics_group.addButton(self.ui.match_averages_radio_button)
        self.statistics_group.addButton(self.ui.match_score_stats_radio_button)
        self.statistics_group.addButton(self.ui.match_highest_out_radio_button)
        self.statistics_group.addButton(self.ui.triples_doubles_radio_button)
        self.statistics_group.addButton(self.ui.player_rank_radio_button)
        self.statistics_group.addButton(self.ui.player_last_win_radio_button)
        self.statistics_group.addButton(self.ui.lifetime_averages_radio_button)
        self.statistics_group.addButton(self.ui.lifetime_scores_radio_button)

        self.enter_start_values()

        
    def enter_start_values(self):
        self.ui.number_of_legs_spin_box.setValue(5)
        self.ui.number_of_sets_spin_box.setValue(5)

        self.ui.leg_value_501_radio_button.setChecked(True)
        self.ui.lifetime_scores_radio_button.setChecked(True)

    def on_navigated_to(self):
        self.populate_player_names("")
        
    def populate_player_names(self, text):
        self.ui.player_one_combo_box.clear()
        self.ui.player_two_combo_box.clear()
        players = search_players(text)
        num_players = len(players)
        for x in players:
            self.ui.player_one_combo_box.addItem(str(x))
            self.ui.player_two_combo_box.addItem(str(x))
        if (num_players >= 2):
            self.ui.player_one_combo_box.setEditText(str(players[0]))
            self.ui.player_two_combo_box.setEditText(str(players[1]))
        else:
            self.ui.player_one_combo_box.setEditText("")
            self.ui.player_two_combo_box.setEditText("")



    def start_game(self):
        print("\n\n")
        
        player_one_name = self.ui.player_one_combo_box.currentText()
        print(player_one_name)
        player_one = get_player_by_full_name(player_one_name)
        print("Number of matches won: {}".format(player_one.number_of_matches_won))

        
        player_two_name = self.ui.player_two_combo_box.currentText()
        print(player_two_name)
        player_two = get_player_by_full_name(player_two_name)


        location = self.ui.location_line_edit.text()
        legs = self.ui.number_of_legs_spin_box.value()
        sets = self.ui.number_of_sets_spin_box.value()
        date = self.ui.date_edit.date().toString("yyyy-MM-dd")

        game_mode = 0

        if self.ui.leg_value_801_radio_button.isChecked():
            game_mode = 801
        elif self.ui.leg_value_501_radio_button.isChecked():
            game_mode = 501
        elif self.ui.leg_value_301_radio_button.isChecked():
            game_mode = 301

        match = create_match(player_one, player_two, sets, legs, game_mode, date)
        match_id = match.id

        checked_radio_button = "lifetime_scores"

        if (self.ui.match_averages_radio_button.isChecked()):
            checked_radio_button = "averages"
        elif (self.ui.match_score_stats_radio_button.isChecked()):
            checked_radio_button = "score_stats"
        elif (self.ui.match_highest_out_radio_button.isChecked()):
            checked_radio_button = "highest_out"
        elif (self.ui.triples_doubles_radio_button.isChecked()):
            checked_radio_button = "triples_doubles"
        elif (self.ui.player_rank_radio_button.isChecked()):
            checked_radio_button = "ranks"
        elif (self.ui.player_last_win_radio_button.isChecked()):
            checked_radio_button = "last_win"
        elif (self.ui.lifetime_averages_radio_button.isChecked()):
            checked_radio_button = "lifetime_averages"

        print(checked_radio_button)



        #get player object through player name

        self.hide()
        self.hub.navigate_to_view("scorer")
        self.hub.navigate_to_view("scoreboard")
        self.hub.send_match_id(match_id)
        self.hub.scoreboard.set_stats_display(checked_radio_button)

        
