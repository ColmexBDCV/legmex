from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from Modules.Registro.models import Registro
from django.views.generic.edit import UpdateView, DeleteView
from Modules.Coleccion.forms import ColectionForm
from Modules.Coleccion.models import Coleccion
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView

# Create your views here.
from Modules.Usuario.models import Perfil


class ColeccionesListView(ListView):
    model = Coleccion
    template_name = "colecciones/show_colection.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ColeccionesListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.groups.filter(name = 'invitado').exists():
            perfil = Perfil.objects.get(usuario = self.request.user)
            return Coleccion.objects.filter(persona = perfil)
        else:
            return Coleccion.objects.all()


class ColeccionesCreateView(SuccessMessageMixin, CreateView):
    form_class = ColectionForm
    template_name = 'colecciones/create_colection.html'
    success_message = 'La coleccion se creó correctamente'
    success_url = '/colections'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ColeccionesCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ColeccionesCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear nueva colección'
        context['user'] = Perfil.objects.get(usuario = self.request.user)
        context['is_create'] = True
        return context

    def form_valid(self, form):
        formpass = form.save(commit = False)
        user = Perfil.objects.get(usuario = self.request.user)
        formpass.persona = user
        formpass.modificado = user
        formpass.save()
        return super(ColeccionesCreateView, self).form_valid(form)

    #def get_form_class(self):
        #return ColectionForm


class ColeccionesUpdateView(SuccessMessageMixin, UpdateView):
    form_class = ColectionForm
    model = Coleccion
    template_name = 'colecciones/create_colection.html'
    success_message = 'La coleccion se actualizó correctamente'
    success_url = '/colections'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ColeccionesUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ColeccionesUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Actualizar datos de la colección'
        context['is_create'] = False
        coleccion =  Coleccion.objects.get(idcoleccion = self.request.resolver_match.kwargs['pk'])
        context['user'] = coleccion.persona
        return context

    def form_valid(self, form):
        formpass = form.save(commit=False)
        user = Perfil.objects.get(usuario=self.request.user)
        formpass.modificado = user
        formpass.save()
        return super(ColeccionesUpdateView, self).form_valid(form)

class ColeccionesDetailView(DetailView):
    model = Coleccion
    template_name = 'colecciones/detail_colection.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return  super(ColeccionesDetailView, self).dispatch(request, *args, **kwargs)

class ColeccionesDeleteView(SuccessMessageMixin, DeleteView):
    model = Coleccion
    success_message = 'Colección Eliminada Correctamente'
    success_url = reverse_lazy('colections')
