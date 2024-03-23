from django.urls import path
from. import views

urlpatterns = [
    path("url/",views.url,name='url'),
    path("bitly-url/",views.bitly,name='bitly'),
]
