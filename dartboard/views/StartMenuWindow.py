from views.StartMenu import Ui_StartMenu
from PySide2.QtWidgets import QApplication, QMainWindow
from backend.generate_players import generate_players
import sys

class StartMenuWindow(QMainWindow):
    def __init__(self, hub):
        super(StartMenuWindow, self).__init__()

        self.hub = hub

        self.ui = Ui_StartMenu()
        self.ui.setupUi(self)
        self.ui.new_match_button.clicked.connect(self.new_match)
        self.ui.manage_players_button.clicked.connect(self.manage_players)
        self.ui.generate_players_button.clicked.connect(self.generate_players)

    def new_match(self):
        self.hide()
        self.hub.navigate_to_view("start_game_configuration")

    def manage_players(self):
        self.hide()
        self.hub.navigate_to_view("manage_players")

    def generate_players(self):
        print("generate_players called")
        generate_players()
        self.hub.manage_players.populate_players()
