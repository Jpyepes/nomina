# Generated by Django 4.1.7 on 2023-04-23 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0003_alter_ordenproduccion_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoorden',
            name='precio',
            field=models.PositiveIntegerField(default=0),
        ),
    ]