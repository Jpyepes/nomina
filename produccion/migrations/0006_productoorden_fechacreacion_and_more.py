# Generated by Django 4.1.7 on 2023-04-25 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0005_rename_productos_productoorden_producto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productoorden',
            name='fechaCreacion',
            field=models.DateField(default='2023-03-17'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productoorden',
            name='fechaEntrega',
            field=models.DateField(default='2023-03-17'),
            preserve_default=False,
        ),
    ]