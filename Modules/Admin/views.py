from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render
from Modules.Coleccion.models import Coleccion, UsuarioInscrito
from Modules.Registro.models import Registro

# Create your views here.
#Vistas basadas en metodos

@login_required
def get_counts(request):
    documentos = Registro.objects.values('tipo_documento__tipo', 'tipo_documento__idTipoDoc').annotate(total = Count('tipo_documento')).order_by
    volumenes = Registro.objects.values('volumen').annotate(total = Count('volumen')).order_by()
    contexto = {
                'docs': documentos,
                'volumenes': volumenes,
            }

    return render(request, 'admin_index.html', contexto)
