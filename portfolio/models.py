from django.db import models


class Home(models.Model):
    facebook_url = models.CharField(max_length=2083, null=True, blank=True, default='')
    instagram_url = models.CharField(max_length=2083, null=True, blank=True, default='')
    whatsapp_url = models.CharField(max_length=2083, null=True, blank=True, default='')
    twitter_url = models.CharField(max_length=2083, null=True, blank=True, default='')
    name = 'urls'

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=30)
    profession = models.CharField(max_length=255)
    about = models.TextField()
    birthday = models.CharField(max_length=255)
    age= models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    platform = models.CharField(max_length=255)


class Service(models.Model):
    service = models.CharField(max_length=50)
    description = models.CharField(max_length=2083)


class Resume(models.Model):
    title = models.CharField(max_length=255)
    higher_edu_title = models.CharField(max_length=255, blank=True)
    higher_edu_description = models.TextField(blank=True)
    university_year = models.CharField(max_length=2083, blank=True)
    inter_edu_title = models.CharField(max_length=255, blank=True)
    inter_edu_description = models.TextField(blank=True)
    college_year = models.CharField(max_length=2083, blank=True)
    metric_edu_title = models.CharField(max_length=255, blank=True)
    metric_edu_description = models.TextField(blank=True)
    school_year = models.CharField(max_length=2083, blank=True)


class Portfolio(models.Model):
    image_url = models.CharField(max_length=2083, blank=True)
    url = models.CharField(max_length=2083, blank=True)
    name = models.CharField(max_length=253)


    def __str__(self):
        return str(self.name)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    content = models.TextField()


    def __str__(self):
        return f'From {self.name}'
