from django.db import models

# Create your models here.


class BlogUser(models.Model):
    name = models.CharField(unique=False, max_length=50)
    email = models.CharField(unique=True, max_length=100)
    contact = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.name