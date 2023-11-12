from django.db import models

# Create your models here
class SentimentVARModel(models.Model):
    game = models.CharField(max_length=100)
    decision = models.CharField(max_length=100)
    commentary = models.CharField(max_length=1000)
    result = models.CharField(max_length=100, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.game