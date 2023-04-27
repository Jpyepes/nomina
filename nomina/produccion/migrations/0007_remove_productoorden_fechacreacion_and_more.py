# Generated by Django 4.1.7 on 2023-04-25 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0006_productoorden_fechacreacion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productoorden',
            name='fechaCreacion',
        ),
        migrations.RemoveField(
            model_name='productoorden',
            name='fechaEntrega',
        ),
        migrations.AddField(
            model_name='ordenproduccion',
            name='fechaCreacion',
            field=models.DateField(default='2023-04-25'),
        ),
        migrations.AddField(
            model_name='ordenproduccion',
            name='fechaEntrega',
            field=models.DateField(default='2023-04-25'),
        ),
    ]
