from django import forms
from django import forms
from django.forms import fields, widgets
from Modules.Coleccion.models import Coleccion
from Modules.Registro.models import Registro

TYPE_CHOICES = (
    ("0", "Privada"),
    ("1", "Publica"),
)

class ColectionForm(forms.ModelForm):
    privada = forms.ChoiceField(choices = TYPE_CHOICES)
    registro = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Registro.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(ColectionForm,self).__init__(*args, **kwargs)

    class Meta:
        model = Coleccion

        fields = [
            'nombre',
            #'persona',
            'registro',
            'privada',
            'descripcion',
        ]

        labels = {
            'nombre': 'Nombre',
            #'persona': 'Autor',
            'registro': 'Selecciona los Registros',
            'privada': 'Tipo de coleccion',
            'descripcion': 'Descripción'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'})
        }