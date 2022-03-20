from django.db import models
from app.validators import phone_number_regex


class AbstractModel(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=500)

    def __str__(self):
        return self.title
    
    class Meta:
        abstract = True



class Message(models.Model):
    name = models.CharField(max_length=25)
    number = models.CharField(max_length=13,validators=[phone_number_regex,])
    email = models.EmailField()
    experience = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=300)
    descriptions2 = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class HomePage(AbstractModel):
    pass


class OurServices(AbstractModel):
    pass


class QuickProjectStart(AbstractModel):
    pass


class Comments(AbstractModel):
    pass
