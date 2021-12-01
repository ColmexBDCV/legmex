from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey, ManyToManyField
from Modules.Usuario.models import Perfil
from Modules.Registro.models import Registro

# Create your models here.

class Coleccion(models.Model):
    idcoleccion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateField(auto_now_add=True)
    privada = models.IntegerField(default=1)
    activa = models.IntegerField(default=1)
    persona = ForeignKey(Perfil, related_name='%(class)s_requests_created', null=False, blank=False, on_delete=models.CASCADE)
    registro = ManyToManyField(Registro, blank=True, null=True)
    descripcion = models.TextField()
    modificado = ForeignKey(Perfil, related_name='%(class)s_requests_modified',null= False, blank=False, on_delete= models.CASCADE)
    fecha_modificacion = models.DateField(auto_now_add=True)
    

class UsuarioInscrito(models.Model):
    idUsuarioInscrito = models.AutoField(primary_key=True)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    coleccion = ForeignKey(Coleccion, null=False, blank=False, on_delete=models.CASCADE)
    usuario = ForeignKey(Perfil, null=False, blank=False, on_delete=models.CASCADE)
