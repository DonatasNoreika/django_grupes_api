from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Band(models.Model):
    name = models.CharField(verbose_name="Name", max_length=150)
    image = models.ImageField(upload_to='pictures', null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(verbose_name="Name", max_length=150)
    band = models.ForeignKey('Band', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(verbose_name="Name", max_length=150)
    duration = models.IntegerField(verbose_name="Duration")
    band = models.ForeignKey('Band', verbose_name="Band", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AlbumReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey('Album', verbose_name="Album", on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    score = models.CharField(verbose_name="Score", max_length=50)

    def __str__(self):
        return f"{self.user} {self.album} review"


class AlbumReviewComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review = models.ForeignKey('AlbumReview', verbose_name="Album Review", on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.user.username}: {self.content}"


class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review = models.ForeignKey('AlbumReview', verbose_name="Album Review", on_delete=models.CASCADE)
