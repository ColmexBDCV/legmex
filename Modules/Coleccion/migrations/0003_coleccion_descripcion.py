# Generated by Django 3.2.7 on 2021-11-08 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coleccion', '0002_rename_legislacion_coleccion_registro'),
    ]

    operations = [
        migrations.AddField(
            model_name='coleccion',
            name='descripcion',
            field=models.TextField(default='descripcion'),
            preserve_default=False,
        ),
    ]
