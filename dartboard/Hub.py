from views.ScorerWindow import ScorerWindow
from views.StartMenuWindow import StartMenuWindow
from views.StartGameConfigurationWindow import StartGameConfigurationWindow
from views.ScoreboardWindow import ScoreboardWindow
from views.ManagePlayersWindow import ManagePlayersWindow

from PySide2.QtGui import QPalette, QColor
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication
import sys

class Hub(QApplication):
    def __init__(self):
        super().__init__()
        self.set_style()


        self.start_menu = StartMenuWindow(self)
        self.start_menu.show()


        self.start_game_configuration = StartGameConfigurationWindow(self)
        #self.start_game_configuration.show()


        self.manage_players = ManagePlayersWindow(self)

    #add functions and high level things here
    def set_style(self):
        self.setStyle("Fusion")
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.black)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(palette)

    def navigate_to_view(self, name):
        if (name == "start_menu"):
            self.start_menu.show()
        elif (name == "start_game_configuration"):
            self.start_game_configuration.on_navigated_to()
            self.start_game_configuration.show()
        elif (name == "scorer"):
            self.scorer = ScorerWindow(self)
            self.scorer.show()
        elif (name == "scoreboard"):
            self.scoreboard = ScoreboardWindow(self)
            self.scoreboard.show()
        elif (name == "manage_players"):
            self.manage_players.populate_players()
            self.manage_players.show()

    def end_game(self):
        self.scorer.close()
        self.scoreboard.close()
        self.navigate_to_view("start_menu")

    def send_match_id(self, match_id):
        print("Match ID: {}".format(match_id))
        self.scoreboard.enter_match_id(match_id)
        self.scorer.enter_match_id(match_id)
        
