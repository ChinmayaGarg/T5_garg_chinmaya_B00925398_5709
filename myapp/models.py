from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    firstName = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.email
