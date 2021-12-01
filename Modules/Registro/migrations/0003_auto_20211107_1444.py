# Generated by Django 3.2.7 on 2021-11-07 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0001_initial'),
        ('Registro', '0002_registro_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='mofificado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='registro_requests_modified', to='Usuario.perfil'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registro',
            name='perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registro_requests_created', to='Usuario.perfil'),
        ),
    ]
