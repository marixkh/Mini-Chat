from django.db import models

class Message(models.Model):
    email = models.EmailField()
    text = models.TextField()