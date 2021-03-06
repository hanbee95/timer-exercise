import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text   
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)        


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class TotalTime(models.Model):
    totalTime = models.IntegerField()

class ExerTime(models.Model):
    # working on this - HAN
    exerid = models.AutoField(primary_key=True)
    setno = models.IntegerField()
    exert = models.IntegerField()
    breakt = models.IntegerField()
    totalt = models.IntegerField()