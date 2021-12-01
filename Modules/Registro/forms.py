from django import forms
from Modules.Registro.models import Registro, Volumen


# class PDFForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(PDFForm, self).__init__(*args, **kwargs)
#
#     class Meta:
#         model = PDF
#
#         fields = [
#             'nombre',
#             'ruta',
#         ]
#
#         labels = {
#             'nombre': 'Nombre',
#             'ruta': 'Agrega un Archivo',
#         }
#
#         widgets = {
#             'nombre': forms.TextInput(attrs={'class': 'form-control'}),
#             'ruta': forms.FileInput(attrs={'class': 'form-control'}),
#         }

class LegislationForm(forms.ModelForm):

    volumen = forms.ModelChoiceField(queryset=Volumen.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(LegislationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Registro
        fields = [
            'titulo',
            'fecha',
            'volumen',
            'pagina_inicio',
            'pagina_final',
            'transcripcion',
            'lugar',
            #'pdf',
            'tipo_documento',
            'relacionado'
        ]

        labels = {
            'titulo': 'Titulo',
            'fecha': 'Fecha',
            'volumen': 'Volumen',
            'pagina_inicio': 'Página de inicio',
            'pagina_final': 'Pagina Final',
            'transcripcion': 'Transcripción',
            'lugar': 'Lugar', 
            #'pdf': 'Elige el PDF asociado',
            'tipo_documento': 'Tipo de documento',
            'relacionado': 'Relacionado con:'
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control datepicker col-10 float-left'}),
            'pagina_inicio': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'pagina_final': forms.NumberInput(attrs={'class': 'form-control'}),
            'transcripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'lugar': forms.TextInput(attrs={'class': 'form-control'}),
            'relacionado': forms.Textarea(attrs={'class': 'form-control', 'rows':2, 'data-role':'tags-input'})
        }

# class CreateLegislacionForm(MultiModelForm):
#     form_classes = {
#         'pdf' : PDFForm,
#         'legislacion' : LegislationForm
#     }

class VolumenForm(forms.ModelForm):

    class Meta:
        def __init__(self, *args, **kwargs):
            return super(VolumenForm, self).__init__(self, *args, **kwargs)

        model = Volumen

        fields = [
            'volumen',
            'paginas',
            'descripcion'
        ]

        labels = {
            'volumen': 'No. Volumen',
            'paginas': 'Total Paginas',
            'descripcion': 'Descripción'
        }

        widgets = {
            'volumen': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'paginas': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'})
        }