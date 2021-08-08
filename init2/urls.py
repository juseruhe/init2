"""init2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from init2.aplicaciones.principal.views import destroy, inicio,create,store,show,edit,update
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #  Persona
    
    path('',inicio,name="index"),
    path('crear/',create,name="create"),
    path('store',store,name="store"),
    path('mostrar/<int:id>/',show,name="show"),
    path('editar/<int:id>/',edit,name="edit"),
    path('update/<int:id>',update,name="update"),
    path('eliminar<int:id>',destroy,name="destroy")
]
