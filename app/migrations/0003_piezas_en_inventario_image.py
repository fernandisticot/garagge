# Generated by Django 2.0 on 2019-07-12 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190628_0434'),
    ]

    operations = [
        migrations.AddField(
            model_name='piezas_en_inventario',
            name='image',
            field=models.ImageField(blank=True, upload_to='pieza_image'),
        ),
    ]
