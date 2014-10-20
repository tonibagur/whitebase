from django.db import models


class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    game_date = models.DateField(null=True)
    event_date = models.DateField(null=True)
    pgn = models.TextField()
    white_player = models.CharField(max_length=100,null=True)
    black_player = models.CharField(max_length=100,null=True)
    event = models.CharField(max_length=100,null=True)
    site = models.CharField(max_length=100,null=True)
    result = models.CharField(max_length=10,null=True)
    white_title = models.CharField(max_length=10,null=True)
    black_title = models.CharField(max_length=10,null=True)
    white_elo = models.FloatField(null=True)
    black_elo = models.FloatField(null=True)
    eco = models.CharField(max_length=10,null=True)
    opening = models.CharField(max_length=100,null=True)
    variation = models.CharField(max_length=100,null=True)
    white_fide_id = models.CharField(max_length=15,null=True)
    black_fide_id = models.CharField(max_length=15,null=True)

    class Meta:
        ordering = ('game_date',)