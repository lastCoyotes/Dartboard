###################
# Describes a player's lifetime data
###################
import uuid
from django.db import models


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    full_name = models.CharField(max_length=512)
    current_league_rank = models.IntegerField()
    average_season_score = models.DecimalField(default=0, decimal_places=10, max_digits=15)
    average_lifetime_score = models.DecimalField(default=0, decimal_places=10, max_digits=15)
    lowest_turn_score = models.IntegerField(default=181)
    number_of_180s = models.IntegerField(default=0)
    number_of_season_turns = models.IntegerField(default=0)
    number_of_lifetime_turns = models.IntegerField(default=0)
    number_of_legs_won = models.IntegerField(default=0)
    number_of_legs_lost = models.IntegerField(default=0)
    number_of_sets_won = models.IntegerField(default=0)
    number_of_sets_lost = models.IntegerField(default=0)
    number_of_matches_won = models.IntegerField(default=0)
    number_of_matches_lost = models.IntegerField(default=0)
    last_win = models.DateField(default=None, null=True)

    def update(self, hits):
        # Generate Score
        score = 0
        for hit in hits:
            score += hit.score

        # Update Season Average
        total_score = self.average_season_score * self.number_of_season_turns
        total_score += score
        self.number_of_season_turns += 1
        self.average_season_score = total_score / self.number_of_season_turns

        # Update Lifetime Average
        total_score = self.average_lifetime_score * self.number_of_lifetime_turns
        total_score += score
        self.number_of_lifetime_turns += 1
        self.average_lifetime_score = total_score / self.number_of_lifetime_turns

        # Update 180s
        if score == 180:
            self.number_of_180s += 1

        # Update Lowest Turn Score
        if score < self.lowest_turn_score:
            self.lowest_turn_score = score

        # Save Results
        self.save()

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
