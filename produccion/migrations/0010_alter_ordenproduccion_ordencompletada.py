# Generated by Django 4.1.7 on 2023-05-03 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0009_rename_stockunidades_producto_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenproduccion',
            name='ordenCompletada',
            field=models.CharField(default='0', max_length=1),
        ),
    ]