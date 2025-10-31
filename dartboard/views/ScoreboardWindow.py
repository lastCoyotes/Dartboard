##################
# ScoreboardWindow
##################

import sys

from backend.fewest_darts import *
from views.Scoreboard import Ui_Scoreboard
from PySide2.QtWidgets import QApplication, QMainWindow, QCheckBox, QTableWidgetItem, QWidget, QHBoxLayout, QHeaderView, QPushButton
from PySide2.QtCore import Qt
from backend.dartboard_api import *


class ScoreboardWindow(QMainWindow):
    def __init__(self, hub):
        super(ScoreboardWindow, self).__init__()

        self.hub = hub
        self.ui = Ui_Scoreboard()
        self.ui.setupUi(self)
        self.tables = [self.ui.Player1DartsTable, self.ui.Player2DartsTable]

        self.current_set = 1
        self.current_leg = 1
        self.ui.player_one_additional_stats.hide()
        self.ui.player_two_additional_stats.hide()
        self.ui.fewest_darts_player_one_label.hide()
        self.ui.fewest_darts_player_two_label.hide()
        self.ui.player_one_win_label.hide()
        self.ui.player_two_win_label.hide()

        self.current_stats_display = ""

    def set_stats_display(self, new_display):
        self.current_stats_display = new_display


    def enter_match_id(self, match_id):
        self.match = get_match_by_id(match_id)
        self.players = get_players_by_match_id(match_id)
        leg = get_leg_by_number(match_id=match_id, set_number=1, leg_number=1)
        
    def clear_scoreboard(self):
        while self.ui.Player1DartsTable.rowCount() > 0:
            self.ui.Player1DartsTable.removeRow(0)
        while self.ui.Player2DartsTable.rowCount() > 0:
            self.ui.Player2DartsTable.removeRow(0)

    def update(self, turn_1, turn_2):
        #update is called in ScorerWindow remove_dart_throw, enter_match_id, and dart_thrown
        self.clear_scoreboard()
        hits_player_1 = get_hits(turn_1)
        hits_player_2 = get_hits(turn_2)
        first_1, second_1, third_1 = "", "-1", ""
        first_2, second_2, third_2 = "", "-1", ""

        #get checkouts for player 1 if applicable
        if (get_turn_score_remaining(turn_1) <= 170):
            # we can call checkout function
            if hits_player_1.count() == 0:
                first_1, second_1, third_1 = check_outs.initial_sum(get_turn_score_remaining(turn_1))
            elif hits_player_1.count() == 1:
                first_1, second_1, third_1 = check_outs.first_sum(get_turn_score_remaining(turn_1), hits_player_1[hits_player_1.count()-1])
            elif hits_player_1.count() == 2:
                first_1, second_1, third_1 = check_outs.second_sum(get_turn_score_remaining(turn_1), hits_player_1[hits_player_1.count() - 2], hits_player_1[hits_player_1.count()-1])
            if first_1 != "":
                self.ui.player_one_checkouts_label.setText("{} | {} | {}".format(first_1, second_1, third_1))
                self.ui.player_one_checkouts_label.show()
            else:
                self.ui.player_one_checkouts_label.hide()
            
        else:
            self.ui.player_one_checkouts_label.hide()

        #get checkouts for player 2 if applicable
        if (get_turn_score_remaining(turn_2) <= 170):
            # we can call checkout function
            if hits_player_2.count() == 0:
                first_2, second_2, third_2 = check_outs.initial_sum(get_turn_score_remaining(turn_2))
            elif hits_player_2.count() == 1:
                first_2, second_2, third_2 = check_outs.first_sum(get_turn_score_remaining(turn_2), hits_player_2[hits_player_2.count()-1])
            elif hits_player_2.count() == 2:
                first_2, second_2, third_2 = check_outs.second_sum(get_turn_score_remaining(turn_2), hits_player_2[hits_player_2.count() - 2], hits_player_2[hits_player_2.count()-1])
            if first_2 != "":
                self.ui.player_two_checkouts_label.setText("{} | {} | {}".format(first_2, second_2, third_2))
                self.ui.player_two_checkouts_label.show()
            else:
                self.ui.player_two_checkouts_label.hide()

        else:
            self.ui.player_two_checkouts_label.hide()

        # print(turn_1.game.leg_number)
        # print(turn_1.player.player.first_name)


        print(fewestdartschecker(get_all_hits_in_leg(turn_1.game, turn_1.player), first_1, second_1, third_1, get_leg_value(turn_1), get_score_remaining(turn_1)))
        if(fewestdartschecker(get_all_hits_in_leg(turn_1.game, turn_1.player), first_1, second_1, third_1, get_leg_value(turn_1), get_score_remaining(turn_1))) and len(get_all_hits_in_leg(turn_1.game, turn_1.player)) != 0:
            self.ui.fewest_darts_player_one_label.show()
        else:
            self.ui.fewest_darts_player_one_label.hide()

        # print(fewestdartschecker(get_all_hits_in_leg(turn_2.game, turn_2.player), first, second, third, get_leg_value(turn_2), get_score_remaining(turn_2)))
        if(fewestdartschecker(get_all_hits_in_leg(turn_2.game, turn_2.player), first_2, second_2, third_2, get_leg_value(turn_2), get_score_remaining(turn_2))) and len(get_all_hits_in_leg(turn_2.game, turn_2.player)) != 0:
            self.ui.fewest_darts_player_two_label.show()
        else:
            self.ui.fewest_darts_player_two_label.hide()


        index = 0

        for hit in hits_player_1:
            self.addpopulaterow(
                self.tables[0], hit.score, hit.is_bounce_out, hit.is_knock_out, hit.is_foul, index)
            index = index+1

        index = 0

        for hit in hits_player_2:
            self.addpopulaterow(
                self.tables[1], hit.score, hit.is_bounce_out, hit.is_knock_out, hit.is_foul, index)
            index = index+1

        # Set Players Name
        self.ui.player_1_name.setText(self.players[0].player.full_name)
        self.ui.player_2_name.setText(self.players[1].player.full_name)

        # Set the players remaining scores
        self.ui.player_1_score.display(str(get_score_remaining(turn_1)))
        self.ui.player_2_score.display(str(get_score_remaining(turn_2)))

        # Update Custom Stats Displays
        self.update_stats_displays(turn_1, turn_2)

    def declare_winner(self, index):
        if (index == 0):
            self.ui.player_one_win_label.setText("<font color='light green'>WINNER</font>")
            self.ui.player_two_win_label.setText("<font color='red'>LOSER</font>")
        elif(index == 1):
            self.ui.player_one_win_label.setText("<font color='red'>LOSER</font>")
            self.ui.player_two_win_label.setText("<font color='light green'>WINNER</font>")
        self.ui.player_one_win_label.show()
        self.ui.player_two_win_label.show()
        
    def update_stats_displays(self, turn_1, turn_2):
        self.ui.player_one_additional_stats.show()
        self.ui.player_two_additional_stats.show()
        if self.current_stats_display == "averages":
            self.ui.player_one_additional_stats.setText("Match Averages: " + str(round(turn_1.player.average_turn_score, 2)))
            self.ui.player_two_additional_stats.setText("Match Averages: " + str(round(turn_2.player.average_turn_score, 2)))
        elif self.current_stats_display == "score_stats":
            self.ui.player_one_additional_stats.setText("Match Score Stats:\nNumber of Sets Complete: " + str(turn_1.player.match.num_sets_complete) + \
                "\nLowest Turn Score: " + str(turn_1.player.lowest_turn_score) + \
                "\nNumber of 180s: " + str(turn_1.player.number_of_180s))
            self.ui.player_two_additional_stats.setText("Match Score Stats:\nNumber of Sets Complete: " + str(turn_2.player.match.num_sets_complete) + \
                "\nLowest Turn Score: " + str(turn_2.player.lowest_turn_score) + \
                "\nNumber of 180s: " + str(turn_2.player.number_of_180s))
        elif self.current_stats_display == "highest_out":
            self.ui.player_one_additional_stats.setText("Match Highest Out: " + str(turn_1.player.highest_out))
            self.ui.player_two_additional_stats.setText("Match Highest Out: " + str(turn_2.player.highest_out))
        elif self.current_stats_display == "triples_doubles":
            self.ui.player_one_additional_stats.setText("Match Doubles: " + str(turn_1.player.number_of_doubles) + \
                "\nMatch Triples: " + str(turn_1.player.number_of_triples))
            self.ui.player_two_additional_stats.setText("Match Doubles: " + str(turn_2.player.number_of_doubles) + \
                "\nMatch Triples: " + str(turn_2.player.number_of_triples))
        elif self.current_stats_display == "ranks":
            self.ui.player_one_additional_stats.setText("Current League Rank: " + str(turn_1.player.player.current_league_rank))
            self.ui.player_two_additional_stats.setText("Current League Rank: " + str(turn_2.player.player.current_league_rank))
        elif self.current_stats_display == "last_win":
            if turn_1.player.player.last_win is None:
                self.ui.player_one_additional_stats.setText("Last Win: Never")
            else:
                self.ui.player_one_additional_stats.setText("Last Win: " + str(turn_1.player.player.last_win))
            if turn_2.player.player.last_win is None:
                self.ui.player_two_additional_stats.setText("Last Win: Never")
            else:
                self.ui.player_two_additional_stats.setText("Last Win: " + str(turn_2.player.player.last_win))
        elif self.current_stats_display == "lifetime_averages":
            self.ui.player_one_additional_stats.setText("Lifetime Average: " + str(round(turn_1.player.player.average_lifetime_score, 2)) + \
                "\nSeason Average: " + str(round(turn_1.player.player.average_season_score, 2)))
            self.ui.player_two_additional_stats.setText("Lifetime Average: " + str(round(turn_2.player.player.average_lifetime_score, 2)) + \
                "\nSeason Average: " + str(round(turn_2.player.player.average_season_score, 2)))
        elif self.current_stats_display == "lifetime_scores":
            self.ui.player_one_additional_stats.setText("Lifetime Lowest Turn: " + str(turn_1.player.player.lowest_turn_score) + \
                "\nLifetime 180s: " + str(turn_1.player.player.number_of_180s))
            self.ui.player_two_additional_stats.setText("Lifetime Lowest Turn: " + str(turn_2.player.player.lowest_turn_score) + \
                "\nLifetime 180s: " + str(turn_2.player.player.number_of_180s))
        else:
            self.ui.player_one_additional_stats.hide()
            self.ui.player_two_additional_stats.hide()






    def addpopulaterow(self, table, value, bounce, knock, foul, index):
        rowPosition = table.rowCount()
        table.insertRow(rowPosition)

        score = QTableWidgetItem()
        score.setTextAlignment(Qt.AlignCenter)
        score.setText(str(value))
        table.setItem(rowPosition, 0, score)

        cell_widget = QWidget()
        chk_bx = QCheckBox()
        if (bounce):
            chk_bx.setCheckState(Qt.Checked)
        else:
            chk_bx.setCheckState(Qt.Unchecked)
        layout = QHBoxLayout(cell_widget)
        layout.addWidget(chk_bx)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        cell_widget.setLayout(layout)
        table.setCellWidget(rowPosition, 1, cell_widget)

        cell_widget = QWidget()
        chk_bx = QCheckBox()
        if (knock):
            chk_bx.setCheckState(Qt.Checked)
        else:
            chk_bx.setCheckState(Qt.Unchecked)
        layout = QHBoxLayout(cell_widget)
        layout.addWidget(chk_bx)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        cell_widget.setLayout(layout)
        table.setCellWidget(rowPosition, 2, cell_widget)

        cell_widget = QWidget()
        chk_bx = QCheckBox()
        if (foul):
            chk_bx.setCheckState(Qt.Checked)
        else:
            chk_bx.setCheckState(Qt.Unchecked)
        layout = QHBoxLayout(cell_widget)
        layout.addWidget(chk_bx)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        cell_widget.setLayout(layout)
        table.setCellWidget(rowPosition, 3, cell_widget)

    def dart_thrown(self, region, score, index):
        self.addpopulaterow(self.tables[0], str(score), False, False, False, index)
