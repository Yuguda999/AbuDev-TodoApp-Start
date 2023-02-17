from django.db import models

from django.contrib.auth.models import User 

class Task (models.Model):
    user = models.OneToOneField ( User , on_delete = models.CASCADE )
    title = models.CharField (max_length = 200)

    def __str__(self):
        return self.title 


