# Generated by Django 4.1.7 on 2023-05-03 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0010_alter_ordenproduccion_ordencompletada'),
    ]

    operations = [
        migrations.AddField(
            model_name='productoorden',
            name='cantidadProducida',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
