from django.db import models

# Create your models here.
class Symbol(models.Model):
  name = models.TextField()
  image = models.ImageField()

  def __str__(self):
    return self.name
