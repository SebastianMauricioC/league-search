from django.db import models


# Create your models here.

class Summoner(models.Model):
    summoner_puuid = models.CharField(max_length=78)
    summoner_name = models.CharField(max_length=30)
    summoner_region = models.CharField(max_length=5)
    summoner_level = models.CharField(max_length=4)
    summoner_icon = models.CharField(max_length=5)


class Champion(models.Model):
    champion_name = models.CharField(max_length=30)
    champion_title = models.CharField(max_length=80)
    champion_attack = models.IntegerField()
    champion_defense = models.IntegerField()
    champion_magic = models.IntegerField()
    champion_difficulty = models.IntegerField()
