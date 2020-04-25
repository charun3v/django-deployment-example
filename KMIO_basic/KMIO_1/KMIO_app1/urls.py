from django.urls import path
from . import views

app_name = 'KMIO_app1'


urlpatterns = [
    path('', views.index, name='index'),
    #path('index', views.index, name='index'),
    path('scheduler', views.scheduler),
    path('info', views.info, name='info'),
    path('patient_id', views.patient_id, name='patient_id'),
    path('register', views.register, name='registrations'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_login', views.user_login, name='user_login'),
]

