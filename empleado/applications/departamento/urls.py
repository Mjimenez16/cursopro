from django.contrib import admin
from django.urls import path, re_path, include

def DesdeApps(self):
    print ('----------------------- desde la app departamentos----------')

urlpatterns = [
    path('departamento/', DesdeApps),
]
