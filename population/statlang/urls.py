
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('stats/',views.stat,name='stat'),
]
