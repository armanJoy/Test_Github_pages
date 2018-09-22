from django.db import models

# Create your models here.

from django.urls import reverse
#
# class cricket(models.Model):
#     Name = models.CharField(max_length=50)
class Match_Regi(models.Model):
    choices = (
        ('a', 'ODI'),
        ('b', 'Test'),
        ('c', 'T20'),
    )
    toss=(
        ('a', 'Team 1'),
        ('b', 'Team 2')
    )
    Match_Name = models.CharField(max_length=1, choices=choices, default='a')
    First_Team_Name = models.CharField(max_length=50, unique=True)
    Second_Team_Name = models.CharField(max_length=50, unique=True)
    Bat_First = models.CharField(max_length=1, choices=toss, default='a')
    Over = models.IntegerField(unique=True)

class Add_Team(models.Model):
    Team1_Player1 = models.CharField(max_length=50)
    Team1_Player2 = models.CharField(max_length=50)
    Team1_Player3 = models.CharField(max_length=50)
    Team1_Player4 = models.CharField(max_length=50)
    Team1_Player5 = models.CharField(max_length=50)
    Team1_Player6 = models.CharField(max_length=50)
    Team1_Player7 = models.CharField(max_length=50)
    Team1_Player8 = models.CharField(max_length=50)
    Team1_Player9 = models.CharField(max_length=50)
    Team1_Player10 = models.CharField(max_length=50)
    Team1_Player11 = models.CharField(max_length=50)
    Team2_Player1 = models.CharField(max_length=50)
    Team2_Player2 = models.CharField(max_length=50)
    Team2_Player3 = models.CharField(max_length=50)
    Team2_Player4 = models.CharField(max_length=50)
    Team2_Player5 = models.CharField(max_length=50)
    Team2_Player6 = models.CharField(max_length=50)
    Team2_Player7 = models.CharField(max_length=50)
    Team2_Player8 = models.CharField(max_length=50)
    Team2_Player9 = models.CharField(max_length=50)
    Team2_Player10 = models.CharField(max_length=50)
    Team2_Player11 = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def get_absolute_url(self):
        return reverse('cricket.views.match_name', args=[self.Match_Name])

    def __str__(self):
        return self.Match_Name

class Go_Live(models.Model):
    name = models.CharField(max_length=10)
