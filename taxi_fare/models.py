from django.db import models



class Journey(models.Model):
    distance = models.FloatField()
    time = models.TimeField()
    fare = models.FloatField(default=0,blank=True,null=True)
    def __str__(self):
        return str(self.distance) + ' ' + str(self.time)