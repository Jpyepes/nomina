# Generated by Django 4.1.7 on 2023-05-09 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0012_ordenproduccion_ordendespacho'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenproduccion',
            name='ordenDespachoCompletada',
            field=models.CharField(default='0', max_length=1),
        ),
    ]