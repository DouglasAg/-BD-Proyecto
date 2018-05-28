"""bases URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from appproyecto import views as proyectoviews
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proyecto/', include('appproyecto.url')),
    url(r'loging/', proyectoviews.loging ),
    url(r'nuevopais/', proyectoviews.nuevopais),
    url(r'cargarpais/', proyectoviews.cargarpais),
    url(r'cargareliminarpais', proyectoviews.cargareliminar),
    url(r'eliminarpais', proyectoviews.eliminarpais),
    url(r'cargarmodificarpais', proyectoviews.cargarmodificarpais),
    url(r'modificarpais', proyectoviews.modificarpais),
    url(r'irpais', proyectoviews.irpais),
    url(r'irpartido', proyectoviews.irpartido),
    url(r'nuevopartido', proyectoviews.nuevopartido),
    url(r'cargarpartidos', proyectoviews.cargarpartidos),
    url(r'cargarmodificarpartido', proyectoviews.cargarmodificarpartido),
    url(r'modificarpartido', proyectoviews.modificarpartido),
    url(r'cargareliminarpartido', proyectoviews.cargareliminarpartido),
    url(r'eliminarpartido', proyectoviews.eliminarpartido),
    url(r'irraza', proyectoviews.irraza),
    url(r'nuevaraza', proyectoviews.nuevaraza),
    url(r'cargarraza', proyectoviews.cargarraza),
    url(r'cargarmodificarraza', proyectoviews.cargarmodificarraza),
    url(r'modificarraza', proyectoviews.modificarraza),
    url(r'cargareliminarraza', proyectoviews.cargareliminarraza),
    url(r'eliminarraza', proyectoviews.eliminarraza),
    url(r'irgenero', proyectoviews.irgenero),
    url(r'nuevagenero', proyectoviews.nuevagenero),
    url(r'cargargenero', proyectoviews.cargargenero),
    url(r'cargarmodificargenero', proyectoviews.cargarmodificargenero),
    url(r'modificargenero', proyectoviews.modificargenero),
    url(r'cargareliminargenero', proyectoviews.cargareliminargenero),
    url(r'eliminargenero', proyectoviews.eliminargenero),
    url(r'irregion',proyectoviews.irregion),
    url(r'cargarpaicesregion', proyectoviews.cargarpaicesregion),
    url(r'nuevaregion', proyectoviews.nuevaregion),
    url(r'cargarregion', proyectoviews.cargarregion),
    url(r'cargarmodificarregion', proyectoviews.cargarmodificarregion),
    url(r'modificaregion', proyectoviews.modificaregion),
    url(r'cargareliminaregion', proyectoviews.cargareliminaregion),
    url(r'eliminarregion', proyectoviews.eliminarregion),
    url(r'irdepartamento', proyectoviews.irdepartamento),
    url(r'nuevodepartamento', proyectoviews.nuevodepartamento),
    url(r'cargardepartamentosver', proyectoviews.cargardepartamentosver),
    url(r'cargardepartamentos', proyectoviews.cargardepartamentos),
    url(r'cargarmodificardepartamento', proyectoviews.cargarmodificardepartamento),
    url(r'modificardepartamento',proyectoviews.modificardepartamento),
    url(r'cargareliminardepartamento', proyectoviews.cargareliminardepartamento),
    url(r'eliminardepartamento', proyectoviews.eliminardepartamento),
    url(r'irmunicipio', proyectoviews.irmunicipio),
    url(r'cargarmunicipiover', proyectoviews.cargarmunicipiover),
    url(r'cargarmunicipios', proyectoviews.cargarmunicipios),
    url(r'nuevomunicipio', proyectoviews.nuevomunicipio),
    url(r'cargarmodificarmunicipio', proyectoviews.cargarmodificarmunicipio),
    url(r'modificarmunicipio', proyectoviews.modificarmunicipio),
    url(r'cargareliminarmunicipio', proyectoviews.cargareliminarmunicipio),
    url(r'eliminarmunicipio', proyectoviews.eliminarmunicipio),
    url(r'ireleccion', proyectoviews.ireleccion),
    url(r'cargarelecciones', proyectoviews.cargarelecciones),
    url(r'nuevaelccion', proyectoviews.nuevaelccion),
    url(r'cargareleccionver', proyectoviews.cargareleccionver),
    url(r'cargarmodificareleccion', proyectoviews.cargarmodificareleccion),
    url(r'modificareleccion', proyectoviews.modificareleccion),
    url(r'cargareliminareleccion', proyectoviews.cargareliminareleccion),
    url(r'eliminareleccion', proyectoviews.eliminareleccion),
]
