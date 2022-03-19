from django.db import models
from app.validators import phone_number_regex

class Message(models.Model):
    name = models.CharField(max_length=25)
    number = models.CharField(max_length=13,validators=[phone_number_regex,])
    email = models.EmailField()
    experience = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Descriptions(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.TextField()

    def __str__(self):
        return self.title


class Title(models.Model):
    descriptions = models.TextField()

    def __str__(self):
        return self.descriptions

