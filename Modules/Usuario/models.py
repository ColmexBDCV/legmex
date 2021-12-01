from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.
# class UserType(models.Model):
#     idType = models.AutoField(primary_key=True)
#     type = models.CharField(max_length=30)
#
#     def __str__(self):
#         txt = "{0}"
#         return txt.format(self.type)

# class Usuario(models.Model):
#     idUsuario = models.AutoField(primary_key=True)
#     usuario = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)
#     type = ForeignKey(UserType, null=False, blank=False, on_delete=models.CASCADE)
#
#     def __str__(self):
#         txt = "{0} ({1})"
#         return txt.format(self.usuario, self.type)

class Perfil(models.Model):
    idPerfil = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    ape_paterno = models.CharField(max_length=100)
    ape_materno = models.CharField(max_length=100)
    fecha_alta = models.DateField(auto_now_add=True)
    usuario = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)

    def nombreCompleto(self):
        nombre = "{0} {1}, {2}"
        return nombre.format(self.ape_paterno, self.ape_materno, self.nombre)
    
    def __str__(self):
        txt = "{0} - {1}"
        return txt.format(self.nombreCompleto(), self.usuario)