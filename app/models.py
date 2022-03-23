from django.db import models


class AbstractModel(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True



class Message(models.Model):
    name = models.CharField(max_length=25)
    number = models.CharField(max_length=13)
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
    descriptions = models.CharField(max_length=200)


class OurServices(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=80)

    def __str__(self):
        return self.title


class QuickProjectStart(models.Model):
    title = models.CharField(max_length=30)
    descriptions = models.CharField(max_length=50)

    def __str__(self):
        return self.title



class Comments(AbstractModel):
    pass


class Contact(models.Model):
    title = models.CharField(max_length=25)
    number = models.IntegerField()

    def __str__(self):
        return self.title
