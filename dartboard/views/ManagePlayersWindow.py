from views.ManagePlayers import Ui_ManagePlayers
from views.NewPlayerWindow import NewPlayerWindow
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton
from PySide2.QtCore import Qt

import sys
from backend.dartboard_api import create_player, get_all_players, get_player_by_full_name, delete_player, edit_player


class ManagePlayersWindow(QMainWindow):
    def __init__(self, hub):
        super(ManagePlayersWindow, self).__init__()

        self.hub = hub

        self.ui = Ui_ManagePlayers()
        self.ui.setupUi(self)

        self.ui.new_player_button.clicked.connect(self.open_new_player_dialog)
        self.ui.return_button.clicked.connect(self.return_to_menu)
        self.ui.players_table_widget.cellClicked.connect(self.cell_clicked)
        self.populate_players()

    def return_to_menu(self):
        self.hub.navigate_to_view("start_menu")
        self.hide()

    def open_new_player_dialog(self):
        self.new_player_dialog = NewPlayerWindow(self)
        self.new_player_dialog.new_player = True
        self.new_player_dialog.show()

    def add_player_to_list(self, first, last):
        print("add player with first name of : {} and last name of {}".format(first, last))
        create_player(first_name=first, last_name=last)
        self.populate_players()

    def modify_existing_player(self, first, last, player):
        edit_player(first, last, player)
        self.populate_players()

    def populate_players(self):
        while self.ui.players_table_widget.rowCount() > 0:
            self.ui.players_table_widget.removeRow(0)
        
        for x in get_all_players():
            self.addpopulaterow(x)

    def addpopulaterow(self, x):
        rowPosition = self.ui.players_table_widget.rowCount()
        self.ui.players_table_widget.insertRow(rowPosition)

        name = QTableWidgetItem()
        name.setTextAlignment(Qt.AlignCenter)
        name.setText(str(x.full_name))
        self.ui.players_table_widget.setItem(rowPosition, 0, name)

        league_rank = QTableWidgetItem()
        league_rank.setTextAlignment(Qt.AlignCenter)
        league_rank.setText(str(x.current_league_rank))
        self.ui.players_table_widget.setItem(rowPosition, 1, league_rank)

        average_season_score = QTableWidgetItem()
        average_season_score.setTextAlignment(Qt.AlignCenter)
        average_season_score.setText(str(round(x.average_season_score,2)))
        self.ui.players_table_widget.setItem(rowPosition, 2, average_season_score)

        average_lifetime_score = QTableWidgetItem()
        average_lifetime_score.setTextAlignment(Qt.AlignCenter)
        average_lifetime_score.setText(str(round(x.average_lifetime_score,2)))
        self.ui.players_table_widget.setItem(rowPosition, 3, average_lifetime_score)

        number_of_180s = QTableWidgetItem()
        number_of_180s.setTextAlignment(Qt.AlignCenter)
        number_of_180s.setText(str(x.number_of_180s))
        self.ui.players_table_widget.setItem(rowPosition, 4, number_of_180s)

        number_of_season_turns = QTableWidgetItem()
        number_of_season_turns.setTextAlignment(Qt.AlignCenter)
        number_of_season_turns.setText(str(x.number_of_season_turns))
        self.ui.players_table_widget.setItem(rowPosition, 5, number_of_season_turns)

        
        cell_widget = QWidget()
        button = QPushButton("X")
        layout = QHBoxLayout(cell_widget)
        layout.addWidget(button)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0,0,0,0)
        cell_widget.setLayout(layout)
        self.ui.players_table_widget.setCellWidget(rowPosition, 6, cell_widget)
        button.clicked.connect(lambda: self.remove_player(x))

    def cell_clicked(self, row, column):
    
        # get player by name
        player = get_player_by_full_name(self.ui.players_table_widget.item(row, 0).text())  

        self.new_player_dialog = NewPlayerWindow(self)
        self.new_player_dialog.ui.first_name_line_edit.setText(player.first_name)
        self.new_player_dialog.ui.last_name_line_edit.setText(player.last_name)
        self.new_player_dialog.player = player
        self.new_player_dialog.setWindowTitle("Edit Existing Player")
        self.new_player_dialog.new_player = False
        self.new_player_dialog.show()
        
    def remove_player(self, player):
        #remove player, then call populate_players again
        delete_player(player)
        self.populate_players()
