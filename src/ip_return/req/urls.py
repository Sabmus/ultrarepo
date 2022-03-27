from django.urls import path
from req import views

app_name='cuisine'
urlpatterns = [
    path('', views.ip_address, name='ip_address'),

]
