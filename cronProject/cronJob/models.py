from django.db import models

# Create your models here.


class PlcMessage(models.Model):
    numDriver = models.IntegerField()
    controlValue = models.FloatField()
    commentStr = models.CharField(max_length=25)

    def __str__(self):
        return str(self.numDriver)
