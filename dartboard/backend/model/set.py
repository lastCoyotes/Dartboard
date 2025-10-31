##################
# Describes a darts set
##################
import uuid
from django.db import models
from backend.model.match import Match


class Set(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    best_of_legs_number = models.IntegerField(default=5)
    num_legs_complete = models.IntegerField(default=0)
    set_number = models.IntegerField(default=1)
