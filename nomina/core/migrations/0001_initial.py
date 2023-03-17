# Generated by Django 4.1.7 on 2023-03-17 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nomina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('extrasDiurnas', models.DecimalField(decimal_places=2, max_digits=3)),
                ('extrasNocturnas', models.DecimalField(decimal_places=2, max_digits=3)),
                ('recargosNocturnos', models.DecimalField(decimal_places=2, max_digits=3)),
                ('horasFestivas', models.DecimalField(decimal_places=2, max_digits=3)),
                ('extrasDF', models.DecimalField(decimal_places=2, max_digits=3)),
                ('extrasNF', models.DecimalField(decimal_places=2, max_digits=3)),
                ('rNF', models.DecimalField(decimal_places=2, max_digits=3)),
                ('devengado', models.DecimalField(decimal_places=2, max_digits=12)),
                ('total', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]
