# Generated by Django 2.0 on 2019-06-28 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='telefono',
        ),
    ]
