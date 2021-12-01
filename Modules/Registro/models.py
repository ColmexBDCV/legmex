import os
from typing_extensions import Required
import uuid
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField, CharField, FilePathField
from django.db.models.fields.related import ForeignKey

# Create your models here.
from Modules.Usuario.models import Perfil


def content_file_name(instance, filename):
    #ext = filename.split('.')[-1]
    #if instance.pk:
        #filename = "%s_%s.%s" % (filename, instance.fk, ext)
    #else:
        #filename = "%s.%s" % (uuid.uuid4().hex, ext)
    return os.path.join('pdf_files', filename)

# class PDF(models.Model):
#     idPdf = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=100)
#     ruta = models.FileField(upload_to = content_file_name)
#
#     def __str__(self):
#         txt = "{0} ({1})"
#         return txt.format(self.nombre, self.ruta)

# class Asunto(models.Model):
#     idAsunto = models.AutoField(primary_key=True)
#     asunto = models.CharField(max_length=200)
#     fecha_alta = models.DateField(auto_now_add=True)
#     fecha_baja = models.DateField()
#     activo = models.IntegerField(default=1)
#
#     def __str__(self):
#         txt = "{0}"
#         return txt.format(self.asunto)

class Volumen(models.Model):
    idVolumen = models.AutoField(primary_key = True)
    volumen = models.IntegerField()
    paginas = models.IntegerField()
    fecha_alta = models.DateField(auto_now=True)
    descripcion = models.TextField()

    def __str__(self):
        text = "{}, Pags. {}"
        return text.format(self.volumen, self.paginas)

class TipoDocumento(models.Model):
    idTipoDoc = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=200)
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField()
    activo = models.IntegerField(default=1)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.tipo)

class Registro(models.Model):
    idRegistro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    fecha = models.DateField()
    #volumen = models.CharField(max_length=30)
    volumen = ForeignKey(Volumen, null=False, blank=False, on_delete=CASCADE)
    pagina_inicio = models.IntegerField()
    pagina_final = models.IntegerField()
    transcripcion = models.TextField()
    lugar = models.CharField(max_length=200)
    #asunto = ForeignKey(Asunto, null=False, blank=False, on_delete=models.CASCADE)
    tipo_documento = ForeignKey(TipoDocumento, null=False, blank= False, on_delete=models.CASCADE)
    #pdf = ForeignKey(PDF, null=False, blank=False, on_delete=models.CASCADE)
    #pdf = models.FileField(upload_to = content_file_name)
    perfil = ForeignKey(Perfil, related_name='%(class)s_requests_created', null=False, blank=False, on_delete=models.CASCADE)
    modificado = ForeignKey(Perfil, related_name='%(class)s_requests_modified', null=False, blank=False, on_delete=models.CASCADE)
    modificado_fecha = models.DateField(auto_now=True)
    relacionado = models.TextField(blank=True)

    def relacionado_list(string):
        return string.split(';')

    def __str__(self):
        txt = "{0} ({1})"
        return txt.format(self.titulo, self.fecha)