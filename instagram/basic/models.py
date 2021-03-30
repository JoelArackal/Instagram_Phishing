from django.db import models
import datetime

# Create your models here.

class UserData(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date_in = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.username


