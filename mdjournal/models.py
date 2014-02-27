from django.db import models

class Post(models.Model):
    Sickness = models.CharField(max_length = 140)
    Doctor = models.CharField(max_length = 100)
    Diagnosis = models.TextField()
    date = models.DateTimeField()

    def __unicode__(self):
        return self.Sickness
