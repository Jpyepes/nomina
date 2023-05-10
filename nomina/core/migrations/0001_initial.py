# Generated by Django 4.1.7 on 2023-04-10 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('cedula', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('salarioBase', models.PositiveIntegerField()),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nomina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('extrasDiurnas', models.DecimalField(decimal_places=2, max_digits=5)),
                ('extrasNocturnas', models.DecimalField(decimal_places=2, max_digits=5)),
                ('recargosNocturnos', models.DecimalField(decimal_places=2, max_digits=5)),
                ('horasFestivas', models.DecimalField(decimal_places=2, max_digits=5)),
                ('extrasDF', models.DecimalField(decimal_places=2, max_digits=5)),
                ('extrasNF', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rNF', models.DecimalField(decimal_places=2, max_digits=5)),
                ('devengado', models.DecimalField(decimal_places=2, max_digits=12)),
                ('total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.empleado')),
            ],
        ),
    ]
