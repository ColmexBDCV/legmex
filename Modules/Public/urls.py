from django.urls import path, include

from Modules.Public.views import corpus_text, add_collection, downlodCollection
from Modules.Usuario.views import registerPublicPage
from Modules.login.views import LoginFormView, LogoutRedirectView, LogoutView

urlpatterns = [
    #path('', LoginFormView.as_view(), name='login')
    path('register/', registerPublicPage, name='register'),
    path('downloadtxt/', corpus_text, name='downloadtxt'),
    path('addcollection/', add_collection, name='addcollection'),
    path('downloadcollection/<int:pk>', downlodCollection, name='downloadcollection'),
]