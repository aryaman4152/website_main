from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=20, null=False)
