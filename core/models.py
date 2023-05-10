from django.db import models

# Create your models here.

class Empleado(models.Model):
    cedula = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    salarioBase = models.PositiveIntegerField()
    fechaInicio = models.DateField()
    fechaFin = models.DateField(null=True)

class Nomina(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    extrasDiurnas = models.DecimalField(max_digits=5,decimal_places=2)
    extrasNocturnas = models.DecimalField(max_digits=5, decimal_places=2)
    recargosNocturnos = models.DecimalField(max_digits=5, decimal_places=2)
    horasFestivas = models.DecimalField(max_digits=5, decimal_places=2)
    extrasDF = models.DecimalField(max_digits=5, decimal_places=2)
    extrasNF = models.DecimalField(max_digits=5, decimal_places=2)
    rNF = models.DecimalField(max_digits=5, decimal_places=2)
    devengado = models.DecimalField(max_digits=12, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2)
