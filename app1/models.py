from django.db import models

GENRE_CHOICES = [
    ('Action', 'Action'),
    ('Comedy', 'Comedy'),
    ('Drama', 'Drama'),
    ('Romance', 'Romance'),
    ('Sci-Fi', 'Sci-Fi'),
    ('Horror', 'Horror'),
    ('Other', 'Other'),
]

class Video(models.Model):
    MovieID = models.AutoField(primary_key=True)
    MovieTitle = models.CharField(max_length=200)
    Actor1Name = models.CharField(max_length=100)
    Actor2Name = models.CharField(max_length=100, blank=True, null=True)
    DirectorName = models.CharField(max_length=100)
    MovieGenre = models.CharField(max_length=50, choices=GENRE_CHOICES, default='Other')
    ReleaseYear = models.PositiveIntegerField()
    DurationMinutes = models.PositiveIntegerField(default=90)


    def __str__(self):
        return f"{self.MovieTitle} ({self.ReleaseYear})"
