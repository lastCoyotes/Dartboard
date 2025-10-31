###################
# Describes a darts match
###################
import uuid
from django.db import models
from django.utils import timezone


class Match(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    best_of_sets_number = models.IntegerField(default=13)
    num_sets_complete = models.IntegerField(default=0)
    match_date = models.DateField(default=timezone.now, null=True)

