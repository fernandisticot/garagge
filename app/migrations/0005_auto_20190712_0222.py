# Generated by Django 2.0 on 2019-07-12 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190712_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piezas_en_inventario',
            name='image',
            field=models.ImageField(default='media/default.jpg', upload_to='media/'),
        ),
    ]
