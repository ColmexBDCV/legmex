# Generated by Django 3.2.7 on 2021-10-19 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Coleccion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coleccion',
            old_name='legislacion',
            new_name='registro',
        ),
    ]
