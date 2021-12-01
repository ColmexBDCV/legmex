from django.urls import path, include

from Modules.Registro.views import VolumenCreateView, VolumenListView, validate_pags, VolumenDeleteView, \
    VolumenUpdateView, RegistroDeleteView
from Modules.login.views import LoginFormView, LogoutRedirectView, LogoutView

urlpatterns = [
    #path('', LoginFormView.as_view(), name='login'),
    path('volumencreate/', VolumenCreateView.as_view(), name='volumencreate'),
    path('volumenlist/', VolumenListView.as_view(), name='volumenlist'),
    path('validatepags/', validate_pags, name="validatepags"),
    path('volumendelete/<int:pk>', VolumenDeleteView.as_view(), name="volumendelete"),
    path('volumenupdate/<int:pk>', VolumenUpdateView.as_view(), name = 'volumenupdate'),
    path('registrodelete/<int:pk>', RegistroDeleteView.as_view(), name='registrodelete'),
]