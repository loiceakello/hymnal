from django.db import models

LANGUAGE_CHOICES = [
    ('dholuo', 'Dholuo'),
    ('kiswahili', 'Kiswahili'),
]

class Hymn(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=200)
    lyrics = models.TextField()
    author = models.CharField(max_length=100, blank=True, null=True)  # optional
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, default="dholuo")  # default to Dholuo
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.number} - {self.title} ({self.language})"

