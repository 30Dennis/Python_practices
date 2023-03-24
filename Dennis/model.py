from __future__ import unicode_literals
from django.db import models


class Students(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=35)
    DOB = models.DateField(max_length=20)

    class Meta:
        db_table = "students"
