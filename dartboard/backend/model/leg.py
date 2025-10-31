import uuid
from django.db import models
from backend.model.set import Set
from backend.model.match_player import MatchPlayer
from backend.model.match import Match


class Leg(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    game_mode = models.IntegerField(default=301)
    player1 = models.ForeignKey(MatchPlayer, related_name="player1", on_delete=models.CASCADE)
    player2 = models.ForeignKey(MatchPlayer, related_name="player2", on_delete=models.CASCADE)
    leg_number = models.IntegerField(default=1)


