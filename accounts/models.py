from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    accountconfigured=models.BooleanField(default=False)
    pass
    # add additional fields in here

    def __str__(self):
        return self.email
    class Meta:
        permissions = (
            ("isTrainer","Trains other users"),
            ("isTrained", "Is trained by others"),
        )
