import uuid
from django.db import models
from backend.model.turn import Turn


##
# This is a basic model class designed to show backend proof of concept
class DartboardHit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    turn = models.ForeignKey(Turn, on_delete=models.CASCADE)
    # Note: I used to have x and y here, however we only really need to keep track of the
    # scores on the backend.
    score = models.IntegerField(default=0)
    is_bounce_out = models.BooleanField(default=False)
    is_knock_out = models.BooleanField(default=False)
    is_foul = models.BooleanField(default=False)
    is_double = models.BooleanField(default=False)
    is_triple = models.BooleanField(default=False)
    is_bullseye = models.BooleanField(default=False)

    def __str__(self):
        return str(self.x) + ', ' + str(self.y)
