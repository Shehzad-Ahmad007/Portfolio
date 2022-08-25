from django.db import models


class Home(models.Model):
    facebook_url = models.CharField(max_length=2083)
    instagram_url = models.CharField(max_length=2083)
    whatsapp_url = models.CharField(max_length=2083)
    name = 'urls'


class About(models.Model):
    name = models.CharField(max_length=30)
    profession = models.CharField(max_length=255)
    about = models.CharField(max_length=2083)
    birthday = models.CharField(max_length=255)
    age= models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    platform = models.CharField(max_length=255)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    content = models.TextField()


    def __str__(self):
        return f'From {self.name}'
