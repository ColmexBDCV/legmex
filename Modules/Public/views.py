import os

from django.db.models import Q, Count
from django.shortcuts import render, redirect
from os.path import basename
from django.conf import settings
from zipfile import ZipFile
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from Modules.Registro.models import Registro, TipoDocumento
from Modules.Coleccion.models import Coleccion
from django.http import HttpResponse, HttpResponseRedirect
from PyPDF2 import PdfFileMerger, PdfFileReader
from django.contrib.staticfiles.storage import staticfiles_storage


###################################################### Vistas basadas en Metodos ###############################################################################################
from Modules.Usuario.models import Perfil


def get_disposiciones_count(request):
    disposiciones = Registro.objects.all()
    tipoDoc =  TipoDocumento.objects.all()
    context = {
        'disposiciones' : disposiciones,
        'tipoDoc' : tipoDoc
    }
    return render(request, 'base.html', context)

def corpus_zip(request):
    #registros = Registro.objects.all()
    #zip_path = createZIP(registros, 'corpus.zip')
    zip_path = createZIPfolder('corpus.zip')
    response = download_file(zip_path, 'corpus.zip')
    return response
    #return redirect('%s%s%s' % (settings.MEDIA_ROOT, 'zip_files', 'corpus.zip'))

def corpus_text(request):
    registros = Registro.objects.all()
    txt_path = createTxt(registros, 'corpus.txt')
    response = download_file(txt_path, 'corpus.txt')
    return response

def createTxt(objects, txt_name):
    txt_path = '%s%s%s' % (settings.MEDIA_ROOT, '/txt_files/',txt_name)
    txt = open(txt_path,"w+")
    try:
        for object in objects:
            txt.write("%s%s"%(object.titulo, '\n'))
            txt.write("%s%s"%(object.transcripcion, '\n\n'))
    finally:
        txt.close()
    return txt_path


def createZIP(object_list, zip_name):
    zip_path = '%s%s%s' % (settings.MEDIA_ROOT, '/zip_files/',zip_name)
    zf = ZipFile(zip_path, mode='w')
    try:
        for object in object_list:
            path = '%s%s%s' % (settings.MEDIA_ROOT, '/', object.pdf)
            zf.write(path, basename(path))
    finally:
        zf.close()
    return zip_path

def createZIPfolder(zip_name):
    zip_path = '%s%s%s' % (settings.MEDIA_ROOT, '/zip_files/', zip_name)
    zf = ZipFile(zip_path, mode='w')
    path_folder = '%s%s' % (settings.MEDIA_ROOT, '/pdf_files/')
    files = os.listdir(path_folder)
    try:
        for f in files:
            path = '%s%s%s' % (path_folder, '/', f)
            zf.write(path, basename(path))
    finally:
        zf.close()
    return zip_path

def download_file(path_f, file_name):
    path_to_file = '%s' % (path_f)
    file_download = open(path_to_file, 'rb')
    #myfile = open(f)
    response = HttpResponse(file_download, content_type='application/force-download') 
    response['Content-Disposition'] = 'attachment; filename=%s' % (file_name)
    #response['X-Sendfile'] = smart_str(path_to_file)
    return response

def add_collection(request):
    idcoleccion = request.POST['coleccion']
    idlegislacion = request.POST['legislacion']
    legislacion = Registro.objects.get(idRegistro = idlegislacion)
    coleccion = Coleccion.objects.get(idcoleccion = idcoleccion)
    user = Perfil.objects.get(usuario = request.user)
    coleccion.modificado = user
    coleccion.save()
    coleccion.registro.add(legislacion)

    return HttpResponseRedirect('/legislacion/%s' %idlegislacion)

def downlodCollection(request, pk):
    collection = Coleccion.objects.get(idcoleccion = pk)
    registers = collection.registro.all()
    txt_name = '%s_%s.txt' %(collection.nombre, collection.idcoleccion)
    txt_path = createTxt(registers, txt_name)
    response = download_file(txt_path, txt_name)
    return response

############################################################# Vistas Basadas en Clases ############################################################

class SearchResultsView(ListView):
    #model = Registro
    template_name = 'public/search_results.html'

    def get_queryset(self):
        q_filter = Q()
        object_list = Registro.objects.none()
        query = self.request.GET.get('query')
        if(query != ''):
            for key in self.request.GET:
                value = self.request.GET[key]
                print(value)
                print(key)
                if(key != 'query' and key != 'title3'):
                    if(key == 'title'):
                        q_filter &= Q(titulo__icontains= query)
                    elif (key == 'title2'):
                        q_filter &= Q(titulo__icontains=query)
                    elif(key == 'place'):
                        q_filter &= Q(lugar__icontains= query)
                    elif(key == 'text'):
                        q_filter &= Q(transcripcion__icontains=query)
                    elif (key == 'dispositionNumber'):
                        q_filter &= Q(idRegistro__icontains=query)
                    else:
                        q_filter &= Q(tipo_documento__tipo=value)
            object_list = Registro.objects.filter(
                q_filter
            )
            print(q_filter)
        return object_list

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query')
        return context

class GetCorpusView(ListView):
    model = Coleccion
    template_name = 'public/download_corpus.html'

    def get_context_data(self, **kwargs):
        context = super(GetCorpusView, self).get_context_data(**kwargs)

        return context

class FilterAsuntosView(ListView):
    template_name = 'public/asuntos.html'

    def get_queryset(self):
        #object_list = Registro.objects.all().select_related('asunto').annotate(total = Count('asunto'))
        object_list = Coleccion.objects.filter(Q(privada = 1)).order_by()
        return object_list

    '''def get_context_data(self, **kwargs):
        context = super(FilterAsuntosView, self).get_context_data(**kwargs)
        context['asuntos'] = Registro.objects.values('asunto__asunto').annotate(total = Count('asunto')).order_by()
        return context'''

class FilterTipoDocView(ListView):
    template_name = 'public/tipo_doc.html'

    def get_queryset(self):
        object_list = Registro.objects.values('tipo_documento__tipo', 'tipo_documento__idTipoDoc').annotate(total = Count('tipo_documento')).order_by()
        return object_list

class TipoDocsByIdView(ListView):
    template_name = 'public/search_results.html'

    def get_queryset(self):
        object_list=Registro.objects.filter(Q(tipo_documento = self.request.resolver_match.kwargs['pk']))
        return object_list

    def get_context_data(self, **kwargs):
        context = super(TipoDocsByIdView, self).get_context_data(**kwargs)
        tipodoc = Registro.objects.filter(Q(tipo_documento = self.request.resolver_match.kwargs['pk'])).values('tipo_documento__tipo').annotate(total = Count('tipo_documento')).order_by()[:1]
        context['query'] = tipodoc[0]['tipo_documento__tipo']
        context['tipo'] = 'por Tipo de Documento'
        return context

class AsuntosByIdView(ListView):
    template_name = 'public/search_results.html'

    def get_queryset(self):
        object_list = Registro.objects.filter(Q(coleccion__idcoleccion = self.request.resolver_match.kwargs['pk']))
        #object_list = Registro.objects.filter(registro__in = colecciones)
        print(object_list)
        return object_list

    def get_context_data(self, **kwargs):
        context = super(AsuntosByIdView, self).get_context_data(**kwargs)
        asuntos = Registro.objects.filter(Q(coleccion__idcoleccion = self.request.resolver_match.kwargs['pk'])).values('coleccion__nombre').annotate(total = Count('coleccion__nombre')).order_by()[:1]
        context['query'] = asuntos[0]['coleccion__nombre']
        context['tipo'] = 'por Colección '
        return context

class FilterByVolumenView(ListView):
    template_name='public/volumen.html'

    def get_queryset(self):
        object_list = Registro.objects.values('volumen__volumen', 'volumen__idVolumen', 'volumen__descripcion').annotate(total = Count('volumen')).order_by()
        return object_list
    
    '''def get_context_data(self, **kwargs):
        context = super(FilterByVolumenView, self).get_context_data(**kwargs)
        return context'''

class VolumenesView(ListView):
    template_name = 'public/search_results.html'

    def get_queryset(self):
        object_list=Registro.objects.filter(Q(volumen__idVolumen = self.request.resolver_match.kwargs['pk']))
        return object_list

    def get_context_data(self, **kwargs):
        context = super(VolumenesView, self).get_context_data(**kwargs)
        volumenes = Registro.objects.filter(Q(volumen__idVolumen = self.request.resolver_match.kwargs['pk'])).values('volumen__volumen').annotate(total = Count('volumen')).order_by()[:1]
        context['query'] = 'Volumen %s'% volumenes[0]['volumen__volumen']
        context['tipo'] = 'por '
        return context

class LegislacionByIdView(DetailView):
    model = Registro
    template_name = 'public/legislacion.html'

    def get_context_data(self, **kwargs):
        context = super(LegislacionByIdView, self).get_context_data(**kwargs)
        data = Registro.objects.filter(Q(idRegistro = self.request.resolver_match.kwargs['pk']))
        volumen = data[0].volumen.volumen
        inicio = data[0].pagina_inicio
        fin = data[0].pagina_final
        merger = PdfFileMerger()
        name = 'legmex-merge-reg%s.pdf'%(data[0].idRegistro)
        path_name = os.path.join(settings.MEDIA_ROOT,'pdf_tmp','legmex-merge-reg%s.pdf'%(data[0].idRegistro))
        if(not os.path.isfile(path_name)):
            for num in range(inicio, fin+1):
                pdf_path = os.path.join(settings.MEDIA_ROOT,'pdf_files/legmex_v%s %s.pdf'%(volumen,num))
                merger.append(PdfFileReader(open(pdf_path, 'rb')))
            merger.write(path_name)
        context['pdf'] = name
        user = Perfil.objects.get(usuario = self.request.user)
        if user.usuario.groups.filter(name='invitado').exists():
            collections = Coleccion.objects.filter(Q(persona = user) & ~Q(registro__idRegistro__contains = self.request.resolver_match.kwargs['pk']))
        else:
            collections = Coleccion.objects.filter(~Q(persona__usuario__groups__name = 'invitado') & ~Q(registro__idRegistro__contains = self.request.resolver_match.kwargs['pk']))
        context['collections'] = collections
        return context

