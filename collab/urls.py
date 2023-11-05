from django.contrib import admin
from django.urls import path, include
from collab.views import *
from allauth.socialaccount.providers.google.urls import urlpatterns as google_urlpatterns

urlpatterns = [
    path('old/', index, name='index.old'),
    path('login/',login, name='login'),
    path('logout/',signout, name='logout'),
    path('', main, name='index'),
    path('api/ai/<str:data>/', VertexAiChat.as_view(), name='ai'),
    path('api/get_device_data/', LoraApi.as_view() , name='get_device_data'), # get device data
    path('api/get_devices/', DevicesApi.as_view() , name='get_devices'), # get devices
    path('accounts/login/', lambda x: redirect('login')), # redirect /accounts/login/ to /login/
    path('accounts/logout/', lambda x: redirect('logout')), # redirect /accounts/logout/ to /logout/
    path('accounts/signup/', lambda x: redirect('login')), # redirect /accounts/signup/ to /login/
    path('accounts/', include('allauth.urls')), # allauth

]
