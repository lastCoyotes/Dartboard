import uuid
from django.db import models
from backend.model.player import Player
from backend.model.match import Match


class MatchPlayer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    average_turn_score = models.DecimalField(default=0, decimal_places=10, max_digits=15)
    number_of_180s = models.IntegerField(default=0)
    number_of_doubles = models.IntegerField(default=0)
    number_of_triples = models.IntegerField(default=0)
    # I'm making this default to 181 since having null data tends to not be great. 181 is an impossible
    # score so if this returns 181, then no lowest score has been set yet
    lowest_turn_score = models.IntegerField(default=181)
    number_of_turns = models.IntegerField(default=0)
    score_remaining = models.IntegerField(default=301)
    leg_wins = models.IntegerField(default=0)
    set_wins = models.IntegerField(default=0)
    highest_out = models.IntegerField(default=0)

    def update(self, hits):
        # Generate Score
        score = 0
        for hit in hits:
            score += hit.score
            if hit.is_double:
                self.number_of_doubles+=1
            if hit.is_triple:
                self.number_of_triples+=1


        # Update Average
        total_score = self.average_turn_score * self.number_of_turns
        total_score += score
        self.number_of_turns += 1
        self.average_turn_score = total_score / self.number_of_turns

        # Update 180s
        if score == 180:
            self.number_of_180s += 1

        # Update Lowest Turn Score
        if score < self.lowest_turn_score:
            self.lowest_turn_score = score

        # Save Results
        self.save()
