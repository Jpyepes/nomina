# Generated by Django 4.1.7 on 2023-04-23 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0002_alter_producto_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenproduccion',
            name='id',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]