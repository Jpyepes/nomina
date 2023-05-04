from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)
    unidades = models.CharField(max_length=3)
    precio = models.PositiveIntegerField(default=0)
    lote = models.PositiveIntegerField(default=0)


class OrdenProduccion(models.Model):
    id = models.AutoField(primary_key=True)
    fechaCreacion = models.DateField(default='2023-04-25')
    fechaEntrega = models.DateField(default='2023-04-25')
    ordenCompletada = models.CharField(max_length=1, default='0')
    
    def devolverProductos(self):
        productos = ProductoOrden.objects.filter(ordenProduccion=self.id)
        return productos


class ProductoOrden(models.Model): 
    cantidadSolicitada = models.PositiveIntegerField()
    cantidadProducida = models.PositiveIntegerField(default=0)
    precio = models.PositiveIntegerField(default=0)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    ordenProduccion = models.ForeignKey(OrdenProduccion, on_delete=models.CASCADE)


'''def save(self, *args, **kwargs):
    if not self.id:
        ultimo_id = OrdenProduccion.objects.all().order_by('-id').first()
        if ultimo_id:
            numero_id = int(ultimo_id.id) + 1
        else:
            numero_id = 1
        self.id = str(numero_id).zfill(5)
    super().save(*args, **kwargs)'''