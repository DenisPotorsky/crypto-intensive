from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.email


