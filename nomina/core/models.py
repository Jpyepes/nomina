from django.db import models

# Create your models here.
class nomina(models.Model):
    nombre = models.CharField(max_length=100)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    extrasDiurnas = models.DecimalField(max_digits=3, decimal_places=2)
    extrasNocturnas = models.DecimalField(max_digits=3, decimal_places=2)
    recargosNocturnos = models.DecimalField(max_digits=3, decimal_places=2)
    horasFestivas = models.DecimalField(max_digits=3, decimal_places=2)
    extrasDF = models.DecimalField(max_digits=3, decimal_places=2)
    extrasNF = models.DecimalField(max_digits=3, decimal_places=2)
    rNF = models.DecimalField(max_digits=3, decimal_places=2)
    devengado = models.DecimalField(max_digits=12, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2)