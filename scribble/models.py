from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.author