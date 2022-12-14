from django.db import models


class WaitlistUser(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=6)
    invited_users = models.CharField(default='', null=True, blank=True, max_length=5000)
    multiplier = models.IntegerField(default=1)

    def __str__(self):
        return self.email
