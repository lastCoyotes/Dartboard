###################
# Contains all of the models
# to be included in the database
###################
import uuid
from django.db import models

# This is the file that django will look for when searching
# for models. In order to have better organization, we
# separate all the models into the model package and then
# import them here so django knows they exist
from backend.model.dartboard_hit import DartboardHit
from backend.model.leg import Leg
from backend.model.match import Match
from backend.model.match_player import MatchPlayer
from backend.model.player import Player
from backend.model.turn import Turn
from backend.model.set import Set
