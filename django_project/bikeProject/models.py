from django.db import models

class Counter(models.Model):
    currentCount = models.IntegerField()

    def __str__(self):
        return "There have been " + str(self.currentCount) + " revolutions"

class Session(models.Model):
    user = models.CharField(max_length=255)
    beginDateTime =  models.DateTimeField(auto_now=False, auto_now_add=False)
    endDateTime =  models.DateTimeField(auto_now=False, auto_now_add=False)
    totalTime = models.IntegerField()
    distanceTraveled = models.IntegerField()
    averageSpeed = models.IntegerField()
    topSpeed = models.IntegerField()

    def __str__(self):
        return "Bike session on " + str(self.beginDateTime) + " lasting " + str(totalTime)

# class User(models.Model):
#     name = models.CharField(max_length=None)

class SelectMode(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    dashboardView = models.BooleanField()
    mapView = models.BooleanField()
    distanceView  = models.BooleanField()
