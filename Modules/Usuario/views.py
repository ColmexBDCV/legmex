from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User,Group
from django.contrib import messages
from Modules.Usuario.forms import  PerfilForm, UsuarioForm, UsuarioUpdateForm
from Modules.Usuario.models import Perfil
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

# Create your views here.
class PersonListView(ListView):
    template_name = 'usuarios/persona_list.html'
    model = Perfil
    active = 'users'
    #def get(self, request, *args, **kwargs):
        #context = locals()
        #context['active'] = self.active
        #return render(self.template_name, context, context_instance=RequestContext(request))

    @method_decorator(login_required)
    @method_decorator(permission_required('perfil.can_view_perfil', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super(PersonListView, self).dispatch(request, *args, **kwargs)

class PersonDetailView(DetailView):
    model = Perfil
    template_name = 'usuarios/detail.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PersonDetailView, self).dispatch(request, *args, **kwargs)


class PersonDeleteView(SuccessMessageMixin,DeleteView):
    model = Perfil
    success_url = reverse_lazy('users')
    success_message = 'El registro se eliminó correctamente'

    def post(self, request, *args, **kwargs):
        id_perfil = request.resolver_match.kwargs['pk']
        usuario = Perfil.objects.filter(idPerfil = id_perfil).values('usuario')
        id_usuario = usuario[0]['usuario']
        user = User.objects.filter(id = id_usuario)
        user.delete()
        return HttpResponseRedirect(reverse_lazy('users'))

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PersonDeleteView, self).dispatch(request, *args, **kwargs)

@login_required
@permission_required('perfil.can_change_perfil', raise_exception=True)
def update_profile(request, pk):
    profile = Perfil.objects.get(idPerfil=pk)
    if request.method == 'POST':
        profile_form = PerfilForm(request.POST, instance=profile)
        user_form = UsuarioUpdateForm(request.POST, instance=profile.usuario)

        if user_form.is_valid() and profile_form.is_valid():
            print('Valid')
            user_form.save()
            profile_form.save()
            messages.success(request, ('El perfil se actualizó correctamente'))
            return redirect('users')
        #else:
            #messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UsuarioForm(instance=profile.usuario)
        profile_form = PerfilForm(instance=profile)
    return render(request, 'usuarios/update.html', {
        'usuario': user_form,
        'perfil': profile_form
    })

def registerPage(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        profile_form = PerfilForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.usuario = user
            profile.save()
            user.groups.add(Group.objects.get(name='editor'))
            messages.success(request,  'La cuenta ha sido creada correctanente')
            return redirect('users')
    else:
        form = UsuarioForm()
        profile_form = PerfilForm()

    context = {'usuario': form, 'perfil': profile_form}
    return render(request, 'usuarios/create.html', context)

def registerPublicPage(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        profile_form = PerfilForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.usuario = user
            profile.save()
            user.groups.add(Group.objects.get(name='invitado'))
            messages.success(request,  'La cuenta ha sido creada correctanente')
            return redirect('login')
    else:
        form = UsuarioForm()
        profile_form = PerfilForm()

    context = {'usuario': form, 'perfil': profile_form}
    return render(request, 'public/new_user.html', context)