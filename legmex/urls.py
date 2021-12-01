"""legmex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Modules.Public.views import FilterByVolumenView, LegislacionByIdView, TipoDocsByIdView, AsuntosByIdView, FilterAsuntosView, FilterTipoDocView, GetCorpusView, SearchResultsView, VolumenesView, corpus_zip, get_disposiciones_count
from Modules.Admin.views import get_counts
from Modules.Registro.views import LegislacionCreateView, LegislacionDetailView, LegislacionesListView, LegislacionesUpdateView
from Modules.Coleccion.views import ColeccionesCreateView, ColeccionesDetailView, ColeccionesListView, ColeccionesUpdateView
from os import name
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from Modules.Usuario.views import (PersonListView,
                                   PersonDetailView,
                                   PersonDeleteView, update_profile, registerPage)
from Modules.login.views import LoginFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('administrator/', get_counts, name = 'administrator'),
    path('login/', include('Modules.login.urls')),
    path('', get_disposiciones_count, name = 'base'),
    path('search/', SearchResultsView.as_view(), name = 'search'),
    path('corpus', GetCorpusView.as_view(), name='corpus'),
    path('downloadcorpus/', corpus_zip, name='downloadcorpus'),
    path('asuntos/', FilterAsuntosView.as_view(), name='asuntos'),
    path('tipodocumentos/', FilterTipoDocView.as_view(), name= 'tipodoc'),
    path('tipodocumento/<int:pk>', TipoDocsByIdView.as_view(), name='tipodocId'),
    path('asunto/<int:pk>', AsuntosByIdView.as_view(), name='asuntosId'),
    path('volumen/', FilterByVolumenView.as_view(), name='volumen'),
    path('volumenes/<int:pk>', VolumenesView.as_view(), name='volumenes'),
    path('users/', PersonListView.as_view(), name='users'),
    path('create/', registerPage, name='create'),
    path('colections/', ColeccionesListView.as_view(), name= 'colections'),
    path('detail/<int:pk>', PersonDetailView.as_view(), name='detail'),
    path('colectionscreate/', ColeccionesCreateView.as_view(), name= 'colectionscreate'),
    path('colectionsupdate/<int:pk>', ColeccionesUpdateView.as_view(), name= 'colectionsupdate'),
    path('colectionsdetail/<int:pk>', ColeccionesDetailView.as_view(), name='colectionsdetail'),
    path('legislations/', LegislacionesListView.as_view(), name = 'legislations'),
    path('legislationscreate/', LegislacionCreateView.as_view(), name= 'legislationscreate'),
    path('legislationsupdate/<int:pk>', LegislacionesUpdateView.as_view(), name='legislationsupdate'),
    path('legislationdetail/<int:pk>', LegislacionDetailView.as_view(), name='legislaciondetail'),
    path('legislacion/<int:pk>', LegislacionByIdView.as_view(), name='legislacionId'),
    # path('pdfs/', PdfListView.as_view(), name='pdfs'),
    # path('pdfcreate/',CreatePDFView.as_view(), name='createpdf'),
    # path('pdfupdate/<int:pk>', UpdatePDFView.as_view(), name='pdfupdate'),
    #path('<slug>/', PersonDetailView.as_view(), name='detail'),
    path('update/<int:pk>', update_profile, name='update'),
    #path('<slug>/delete', PersonDeleteView.as_view(), name='delete'),
    path('registro/', include('Modules.Registro.urls')),
    path('collections/', include('Modules.Coleccion.urls')),
    path('users/', include('Modules.Usuario.urls')),
    path('register/', include('Modules.Public.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)