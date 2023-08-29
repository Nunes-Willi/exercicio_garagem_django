from django.db import models

from uploader.models import Image

from garagem.models import Modelo, Cor, Acessorio


class Veiculo(models.Model):
    modelo = models.ForeignKey(
        Modelo, on_delete=models.PROTECT, related_name="veiculos"
    )
    cor = models.ForeignKey(
        Cor, on_delete=models.PROTECT, related_name="veiculos"
    )
    ano = models.IntegerField(default=0, null=True, blank=True,)

    preco = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, null=True, blank=True)

    acessorio = models.ManyToManyField(Acessorio, related_name="Acessórios")

    imagem = models.ManyToManyField(Image, related_name="Veículo")

    def __str__(self):
        return f"{self.modelo}, {self.marca}, {self.ano}, {self.cor}, ({self.id})"
    class Meta:
        verbose_name = "Veículo"