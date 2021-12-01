from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView, DeleteView
from Modules.Registro.forms import LegislationForm, VolumenForm
from Modules.Registro.models import Registro, Volumen
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy

# Create your views here.
from Modules.Usuario.models import Perfil


class LegislacionesListView(ListView):
    model = Registro
    template_name = 'legislaciones/list_legislations.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LegislacionesListView, self).dispatch(request, *args, **kwargs)

class LegislacionCreateView(SuccessMessageMixin,CreateView):
    form_class = LegislationForm
    template_name = 'legislaciones/legislation_create.html'
    success_message = 'Se creo el registro correctamente'
    success_url = reverse_lazy('legislations')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LegislacionCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LegislacionCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear nuevo Registro'
        return context

    def form_valid(self, form):
        form_reg = form.save(commit = False)
        perfil = Perfil.objects.get(usuario = self.request.user)
        form_reg.perfil = perfil
        form_reg.modificado = perfil
        form_reg.save()
        return super(LegislacionCreateView, self).form_valid(form)

    #Se comenta el metodo para recibir los datos del formulario PDF, se puede guardar juntos con Registro
    '''
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            pdf = form['pdf'].save()
            legislacion = form['legislacion'].save(commit = False)
            legislacion.pdf = pdf
            legislacion.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
            '''

class LegislacionesUpdateView(SuccessMessageMixin,UpdateView):
    form_class = LegislationForm
    model = Registro
    template_name = 'legislaciones/legislation_create.html'
    success_url = '/legislations'
    success_message = 'Registro Actualizado Correctamente'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return  super(LegislacionesUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LegislacionesUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Actualizar datos del Registro'
        return context

    def form_valid(self, form):
        form_reg = form.save(commit = False)
        perfil = Perfil.objects.get(usuario = self.request.user)
        form_reg.modificado = perfil
        form_reg.save()
        return super(LegislacionesUpdateView, self).form_valid(form)

# class PdfListView(ListView):
#     model = PDF
#     template_name = 'pdfs/pdf_list.html'
#
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super(PdfListView, self).dispatch(request, *args, **kwargs)
#
# class CreatePDFView(CreateView):
#     form_class = PDFForm
#     template_name = 'pdfs/create_pdf.html'
#     success_url = '/pdfs'
#
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super(CreatePDFView, self).dispatch(request, *args, **kwargs)
#
# class UpdatePDFView(UpdateView):
#     form_class = PDFForm
#     model = PDF
#     template_name = 'pdfs/create_pdf.html'
#     success_url = '/pdfs'
#
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super(UpdatePDFView, self).dispatch(request, *args, **kwargs)

class LegislacionDetailView(DetailView):
    model = Registro
    template_name = 'legislaciones/legislation_detail.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LegislacionDetailView, self).dispatch(request, *args, **kwargs)

class RegistroDeleteView(SuccessMessageMixin, DeleteView):
    model = Registro
    success_url = reverse_lazy('legislations')
    success_message = 'El registro se eliminó correctamente'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(RegistroDeleteView, self).dispatch(request, *args, **kwargs)

class VolumenCreateView(SuccessMessageMixin, CreateView):
    form_class = VolumenForm
    template_name = 'volumen/volumen_create.html'
    success_message = 'Volumen agregado correctamente'
    success_url = reverse_lazy('volumenlist')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(VolumenCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(VolumenCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Alta de Volumen'
        return context

class VolumenUpdateView(SuccessMessageMixin, UpdateView):
    model = Volumen
    form_class = VolumenForm
    template_name = 'volumen/volumen_create.html'
    success_message = 'Volumen actualizado correctamente'
    success_url = reverse_lazy('volumenlist')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(VolumenUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(VolumenUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Actualizar Volumen'
        return context

class VolumenListView(SuccessMessageMixin, ListView):
    model = Volumen
    template_name = 'volumen/volumenes.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(VolumenListView, self).dispatch(request, *args, **kwargs)

class VolumenDeleteView(SuccessMessageMixin, DeleteView):
    model = Volumen
    success_url = reverse_lazy('volumenlist')
    success_message = 'El registro se eliminó correctamente'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(VolumenDeleteView, self).dispatch(request, *args, **kwargs)

@login_required
def validate_pags(request):
    if(request.method == 'GET'):
        volumen = request.GET.get('volumen')
        paginas = Volumen.objects.filter(Q(idVolumen = volumen)).values('paginas')
        return JsonResponse({"total": paginas[0]['paginas']})