import uuid
from django.db import models
from backend.model.match_player import MatchPlayer
from backend.model.leg import Leg


class Turn(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game = models.ForeignKey(Leg, on_delete=models.CASCADE)
    player = models.ForeignKey(MatchPlayer, on_delete=models.CASCADE)
    is_bust = models.BooleanField(default=False)
    is_committed = models.BooleanField(default=False)
