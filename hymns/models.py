from django.db import models

class Hymn(models.Model):
    title = models.CharField(max_length=200)
    lyrics = models.TextField()
    number = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.number}: {self.title}" 

