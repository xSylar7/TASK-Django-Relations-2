from email.policy import default
from django.db import models

# CREATE YOUR RELATION HERE
class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    
    name = models.CharField(max_length=150)
    image = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Category: {self.name}"

class Item(models.Model):
    name = models.CharField(max_length=150)
    image = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name



