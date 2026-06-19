from django.db import models

class Comment(models.Model):
    name = models.CharField()
    text = models.TextField()
