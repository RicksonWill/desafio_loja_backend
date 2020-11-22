from django.db import models

class Produto(models.Model):
  name = models.CharField(max_length=30)
  cod = models.CharField(max_length=30)
  value = models.FloatField()
  qtd = models.IntegerField()

  def __str__(self):
    return self.name

