from django.db import models

# Create your models here.
class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_func = models.CharField(max_length=200)
    idade_min = models.IntegerField()
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome