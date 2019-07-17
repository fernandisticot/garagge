# Generated by Django 2.0 on 2019-06-28 03:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Depositos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('monto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Horas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('precio', models.IntegerField(default=0)),
                ('fecha', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Piezas_en_inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_serie', models.CharField(default='o00000o', max_length=30)),
                ('marca', models.CharField(default='000000', max_length=30)),
                ('modelo', models.CharField(default='000000', max_length=30)),
                ('ubicacion', models.CharField(default='o00000o', max_length=30)),
                ('precio', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('descripcion', models.CharField(default=' no hay descripcion', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Piezas_usadas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_serie', models.CharField(max_length=30, null=True)),
                ('precio', models.IntegerField(default=0)),
                ('descripcion', models.CharField(default=' no hay descripcion', max_length=30)),
                ('marca', models.CharField(default='000000', max_length=30)),
                ('modelo', models.CharField(default='000000', max_length=30)),
                ('cantidad', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PiezaUso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esutilizable', models.BooleanField(default=True)),
                ('pieza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Piezas_en_inventario')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('terminado', models.BooleanField(default=False)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Auto')),
            ],
        ),
        migrations.CreateModel(
            name='Usos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usos', models.CharField(max_length=52)),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=512)),
                ('monto', models.IntegerField(default=0)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Cliente')),
            ],
        ),
        migrations.AddField(
            model_name='piezauso',
            name='uso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Usos'),
        ),
        migrations.AddField(
            model_name='piezas_usadas',
            name='trabajo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Trabajo'),
        ),
        migrations.AddField(
            model_name='horas',
            name='trabajo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Trabajo'),
        ),
        migrations.AddField(
            model_name='depositos',
            name='trabajo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Trabajo'),
        ),
        migrations.AddField(
            model_name='auto',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Cliente'),
        ),
    ]