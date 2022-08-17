from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    content = models.TextField()


    def __str__(self):
        return f'From {self.name}'
