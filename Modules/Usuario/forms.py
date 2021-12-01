from django import forms
from Modules.Usuario.models import Perfil
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PerfilForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Perfil

        fields = [
            'nombre',
            'ape_paterno',
            'ape_materno',
        ]

        labels = {
            'nombre': 'Nombre',
            'ape_paterno': 'Apellido Paterno',
            'ape_materno': 'Apellido Materno',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'autofocus':''}),
            'ape_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'ape_materno': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UsuarioForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = User
        #type = forms.ModelChoiceField(queryset=UserType.objects.all(),empty_label=None, to_field_name="user_type")
        fields = [
            'username',
            'password1',
            'password2',
            'email',
        ]

        labels = {
            'user': 'Usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
            'email': 'Email',
            #'type': 'Tipo de Usuario',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            #'type': forms.ModelChoiceField(queryset=UserType.objects.all(), empty_label=None, to_field_name="user_type"),
        }


class UsuarioUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioUpdateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        # type = forms.ModelChoiceField(queryset=UserType.objects.all(),empty_label=None, to_field_name="user_type")
        fields = [
            'username',
            'email',
        ]

        labels = {
            'user': 'Usuario',
            'email': 'Email',
            # 'type': 'Tipo de Usuario',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'type': forms.ModelChoiceField(queryset=UserType.objects.all(), empty_label=None, to_field_name="user_type"),
        }

