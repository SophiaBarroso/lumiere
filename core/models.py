from django.db import models

class Genero(models.Model):
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.genero

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, related_name="Filme")
    duracao = models.DurationField()
    data_de_lancamento = models.DateField()

    def __str__(self):
        return self.titulo

class Artista(models.Model):
    nome = models.CharField(max_length=100)
    personagem = models.CharField(max_length=100)
    filme = models.ForeignKey(Filme, on_delete=models.PROTECT, related_name="Artista")

    def __str__(self):
        return f'{self.nome} ({self.filme})'