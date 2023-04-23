from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    stockUnidades = models.PositiveIntegerField(default=0)
    stockGramos = models.FloatField(default=0)
    precio = models.PositiveIntegerField(default=0)


class OrdenProduccion(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            ultimo_id = OrdenProduccion.objects.all().order_by('-id').first()
            if ultimo_id:
                numero_id = int(ultimo_id.id) + 1
            else:
                numero_id = 1
            self.id = str(numero_id).zfill(5)
        super().save(*args, **kwargs)

class ProductoOrden(models.Model):
    cantidadSolicitada = models.PositiveIntegerField()
    precio = models.PositiveIntegerField(default=0)
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE)
    ordenProduccion = models.ForeignKey(OrdenProduccion, on_delete=models.CASCADE)