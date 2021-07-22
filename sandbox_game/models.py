from django.db import models


class Game(models.Model):
    gameID = models.CharField(max_length=50)
    
    def __str__(self):
        return self.gameID


class Team(models.Model):
    teamName = models.CharField(max_length=10)

    def __str__(self):
        return self.teamName

class Player(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name