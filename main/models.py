from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Item(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField()
    picked = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=True,
        related_name="picked_items"
    )
