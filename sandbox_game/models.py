from django.db import models


class Player(models.Model):
    playerName = models.CharField(max_length=10, default="", primary_key=True)
    teamName = models.CharField(max_length=10, default="")
    gameID = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.playerName