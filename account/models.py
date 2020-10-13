from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    birthday = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=11, null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)
