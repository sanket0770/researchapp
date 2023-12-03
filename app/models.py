from django.db import models

# Create your models here.
class recipebook(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    ingredient = models.CharField(max_length=100)
    recipe = models.CharField(max_length=5000)
    image = models.CharField(max_length=3000)

    def __str__(self):
        return self.name