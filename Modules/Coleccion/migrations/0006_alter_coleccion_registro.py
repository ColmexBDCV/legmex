# Generated by Django 3.2.9 on 2021-11-24 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0009_alter_registro_relacionado'),
        ('Coleccion', '0005_alter_coleccion_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coleccion',
            name='registro',
            field=models.ManyToManyField(blank=True, null=True, to='Registro.Registro'),
        ),
    ]
