from django.urls import path, include

from Modules.Coleccion.views import ColeccionesDeleteView

urlpatterns = [
    #path('', LoginFormView.as_view(), name='login')
    path('collectiondelete/<int:pk>', ColeccionesDeleteView.as_view(), name='collectiondelete'),
]