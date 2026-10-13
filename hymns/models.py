# from django.db import models

# class Hymn(models.Model):
#     title = models.CharField(max_length=200)
#     lyrics = models.TextField()
#     number = models.IntegerField(unique=True)

#     def __str__(self):
#         return f"{self.number}: {self.title}" 



from django.db import models

class Hymn(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=200)
    lyrics = models.TextField()
    author = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=50, default="dholuo")  # default to Dholuo
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.number} - {self.title} ({self.language})"

