# Generated by Django 4.1.7 on 2023-04-26 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0008_ordenproduccion_ordencompletada'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='stockUnidades',
            new_name='stock',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='stockGramos',
        ),
        migrations.AddField(
            model_name='producto',
            name='unidades',
            field=models.CharField(default='Und', max_length=3),
            preserve_default=False,
        ),
    ]
