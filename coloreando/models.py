from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    color = models.CharField(max_length=7, default="#000000", editable=True)

    def __unicode__(self):
        return self.username