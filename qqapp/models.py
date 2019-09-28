from django.conf import settings
from django.db import models
from django.utils import timezone


class Qq(models.Model):
    qqname = models.CharField(max_length=200)
    qq_date = models.CharField(max_length=10)
    qq_desc = models.TextField()
    qq_que = models.BooleanField()
    qq_can = models.BooleanField()
    qq_logo = models.CharField(max_length=200)
    qq_pic = models.CharField(max_length=800, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.qqname