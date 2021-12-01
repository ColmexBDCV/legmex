from django.urls import path, include

from Modules.Usuario.views import PersonDeleteView
from Modules.login.views import LoginFormView, LogoutRedirectView, LogoutView

urlpatterns = [
    #path('', LoginFormView.as_view(), name='login'),
    path('userdelete/<int:pk>', PersonDeleteView.as_view(), name='userdelete'),
]