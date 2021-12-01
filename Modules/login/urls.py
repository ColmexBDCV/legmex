from django.urls import path, include

from Modules.login.views import LoginFormView, LogoutRedirectView, LogoutView

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    #path('logout/', LogoutView.as_view(pattern_name = 'login'), name='logout'),
    path('logout/', LogoutRedirectView.as_view(), name='logout'),
]