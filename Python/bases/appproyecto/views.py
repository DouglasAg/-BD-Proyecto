from django.shortcuts import render, HttpResponse
from .models import Pais, Partido, Raza, Genero, Region, Departamento, Municipio, Eleccion


# Create your views here.

def home(request):
    return render(request, 'login.html')

def irpais(request):
    return render(request, 'pais.html')

def irpartido(request):
    return render(request, 'partido.html')

def irraza(request):
    return render(request, 'raza.html')

def irgenero(request):
    return render(request, 'genero.html')

def irregion(request):
    return render(request, 'region.html')

def irdepartamento(request):
    return render(request, 'departamento.html')

def irmunicipio(request):
    return render(request, 'municipio.html')

def ireleccion(request):
    return render(request, 'eleccion.html')

def loging(request):
    if request.method == 'POST':
        nombre = request.POST['username']
        clave = request.POST['pass']
        confirmacion = False
        print(nombre + clave)
        if nombre == "admin" and clave == "admin":
            temporales = Pais.objects.all()
            return render(request, 'pais.html')
    return render(request, 'login.html',{'confirmacion': confirmacion})


def mostrartemporal(request):
    temporales = Temporal.objects.all()

def nuevopais(request):
    if request.method == 'POST':
        nombre = request.POST['pais']
        print(nombre)
        nuevo = Pais(nombre_pais=nombre)
        nuevo.save()
        paisnuevo = True
        return render(request, 'pais.html', {'paisnuevo':paisnuevo})

def cargarpais(request):
    if request.method == 'POST':
        paices = Pais.objects.order_by('id_pais')
        return render(request, 'pais.html',{'paices':paices})


def cargareliminar(request):
    if request.method == 'POST':
        paices = Pais.objects.order_by('id_pais')
        return render(request, 'pais.html',{'paiceselim':paices})

def eliminarpais(request):
    if request.method == 'POST':
        nombre = request.POST['paiselim']
        print(nombre)
        Pais.objects.filter(id_pais=nombre).delete()
        eliminado = True
        return render(request, 'pais.html', {'eliminado':eliminado})

def cargarmodificarpais(request):
    if request.method == 'POST':
        paices = Pais.objects.order_by('id_pais')
        return render(request, 'pais.html',{'paicesmod':paices})

def modificarpais(request):
    if request.method == 'POST':
        pais = request.POST['pais']
        idpais = request.POST['paismod']
        Pais.objects.filter(id_pais = idpais).update(nombre_pais = pais)
        return render(request, 'pais.html',{'modificado':True})

def nuevopartido(request):
    if request.method == 'POST':
        siglas = request.POST['siglas']
        nombre = request.POST['partido']
        nuevo = Partido(iniciales_partido=siglas, nombre_partido=nombre)
        nuevo.save()
        nuevopar = True
        return render(request, 'partido.html', {'nuevopar':nuevopar})

def cargarpartidos(request):
    if request.method == 'POST':
        partidos = Partido.objects.order_by('id_partido')
        return render(request, 'partido.html',{'partidos':partidos})

def cargarmodificarpartido(request):
    if request.method == 'POST':
        partidos = Partido.objects.order_by('id_partido')
        return render(request, 'partido.html',{'partidosmod':partidos})

def modificarpartido(request):
    if request.method == 'POST':
        siglas = request.POST['siglas']
        nombre = request.POST['partido']
        idpartido = request.POST['partidomod']
        if nombre != "" and siglas != "":
            Partido.objects.filter(id_partido = idpartido).update(iniciales_partido = siglas, nombre_partido = nombre)
            return render(request, 'partido.html',{'modificado':True})
        if nombre != "" and siglas == "":
            Partido.objects.filter(id_partido = idpartido).update(nombre_partido = nombre)
            return render(request, 'partido.html',{'modificado':True})
        if nombre == "" and siglas != "":
            Partido.objects.filter(id_partido = idpartido).update(iniciales_partido = siglas)
            return render(request, 'partido.html',{'modificado':True})
        return render(request, 'partido.html',{'modificado':False})

def cargareliminarpartido(request):
    if request.method == 'POST':
        partidos = Partido.objects.order_by('id_partido')
        return render(request, 'partido.html',{'partidoelim':partidos})

def eliminarpartido(request):
    if request.method == 'POST':
        idpartido = request.POST['partidoelim']
        Partido.objects.filter(id_partido=idpartido).delete()
        eliminado = True
        return render(request, 'partido.html', {'eliminado':eliminado})

def nuevaraza(request):
    if request.method == 'POST':
        raza = request.POST['raza']
        nueva = Raza(nombre_raza=raza)
        nueva.save()
        return render(request, 'raza.html', {'razanueva':True})

def cargarraza(request):
    if request.method == 'POST':
        razas = Raza.objects.order_by('id_raza')
        return render(request, 'raza.html',{'razas':razas})

def cargarmodificarraza(request):
    if request.method == 'POST':
        razas = Raza.objects.order_by('id_raza')
        return render(request, 'raza.html',{'razasmod':razas})

def modificarraza(request):
    if request.method == 'POST':
        raza = request.POST['raza']
        idraza = request.POST['razamod']
        Raza.objects.filter(id_raza = idraza).update(nombre_raza = raza)
        return render(request, 'raza.html',{'modificado':True})

def cargareliminarraza(request):
    if request.method == 'POST':
        razas = Raza.objects.order_by('id_raza')
        return render(request, 'raza.html',{'razaseli':razas})

def eliminarraza(request):
    if request.method == 'POST':
        idraza = request.POST['razaeli']
        Raza.objects.filter(id_raza=idraza).delete()
        eliminado = True
        return render(request, 'raza.html', {'eliminado':eliminado})

def nuevagenero(request):
    if request.method == 'POST':
        genero = request.POST['genero']
        nueva = Genero(nombre_genero=genero)
        nueva.save()
        return render(request, 'genero.html', {'generonueva':True})

def cargargenero(request):
    if request.method == 'POST':
        generos = Genero.objects.order_by('id_genero')
        return render(request, 'genero.html',{'generos':generos})

def cargarmodificargenero(request):
    if request.method == 'POST':
        generos = Genero.objects.order_by('id_genero')
        return render(request, 'genero.html',{'generosmod':generos})

def modificargenero(request):
    if request.method == 'POST':
        genero = request.POST['genero']
        idgenero = request.POST['generomodi']
        Genero.objects.filter(id_genero = idgenero).update(nombre_genero = genero)
        return render(request, 'genero.html',{'modificado':True})

def cargareliminargenero(request):
    if request.method == 'POST':
        generos = Genero.objects.order_by('id_genero')
        return render(request, 'genero.html',{'generoseli':generos})

def eliminargenero(request):
    if request.method == 'POST':
        idgenero = request.POST['generoeli']
        Genero.objects.filter(id_genero=idgenero).delete()
        eliminado = True
        return render(request, 'genero.html', {'eliminado':eliminado})

def cargarpaicesregion(request):
    if request.method == 'POST':
        paices = Pais.objects.order_by('id_pais')
        return render(request, 'region.html',{'paices':paices})

def nuevaregion(request):
    if request.method == 'POST':
        idpais = request.POST['paisid']
        region = request.POST['region']
        pais = Pais.objects.get(id_pais=idpais)
        nueva = Region(nombre_region = region, pais_id_pais = pais)
        nueva.save()
        return render(request, 'region.html', {'regionnueva':True})

def cargarregion(request):
    if request.method == 'POST':
        regiones = Region.objects.order_by('id_region')
        return render(request, 'region.html',{'regiones':regiones})

def cargarmodificarregion(request):
    if request.method == 'POST':
        regiones = Region.objects.order_by('id_region')
        return render(request, 'region.html',{'regionesmod':regiones})

def modificaregion(request):
    if request.method == 'POST':
        region = request.POST['region']
        idregion = request.POST['regionmodi']
        Region.objects.filter(id_region = idregion).update(nombre_region = region)
        return render(request, 'region.html',{'modificado':True})

def cargareliminaregion(request):
    if request.method == 'POST':
        regiones = Region.objects.order_by('id_region')
        return render(request, 'region.html',{'regioneli':regiones})

def eliminarregion(request):
    if request.method == 'POST':
        idregion = request.POST['regioneli']
        Region.objects.filter(id_region=idregion).delete()
        eliminado = True
        return render(request, 'region.html', {'eliminado':eliminado})

def cargardepartamentos(request):
    if request.method == 'POST':
        regiones = Region.objects.order_by('id_region')
        return render(request, 'departamento.html',{'regiones':regiones})

def nuevodepartamento(request):
    if request.method == 'POST':
        idregion = request.POST['regionid']
        departamento = request.POST['departamento']
        region = Region.objects.get(id_region=idregion)
        nueva = Departamento(nombre_departamento = departamento, region_id_region = region)
        nueva.save()
        return render(request, 'departamento.html', {'departamentonueva':True})

def cargardepartamentosver(request):
    if request.method == 'POST':
        departamentos = Departamento.objects.order_by('id_departamento')
        return render(request, 'departamento.html',{'departamentos':departamentos})

def cargarmodificardepartamento(request):
    if request.method == 'POST':
        departamentos = Departamento.objects.order_by('id_departamento')
        return render(request, 'departamento.html',{'departamentosmod':departamentos})

def modificardepartamento(request):
    if request.method == 'POST':
        departamento = request.POST['departamento']
        iddepartamento = request.POST['departamentomodi']
        Departamento.objects.filter(id_departamento = iddepartamento).update(nombre_departamento = departamento)
        return render(request, 'departamento.html',{'modificado':True})

def cargareliminardepartamento(request):
    if request.method == 'POST':
        departamentos = Departamento.objects.order_by('id_departamento')
        return render(request, 'departamento.html',{'departamentoeli':departamentos})

def eliminardepartamento(request):
    if request.method == 'POST':
        iddepartamento = request.POST['departamentoeli']
        Departamento.objects.filter(id_departamento=iddepartamento).delete()
        eliminado = True
        return render(request, 'departamento.html', {'eliminado':eliminado})

def cargarmunicipios(request):
    if request.method == 'POST':
        departamentos = Departamento.objects.order_by('id_departamento')
        return render(request, 'municipio.html',{'departamentos':departamentos})

def nuevomunicipio(request):
    if request.method == 'POST':
        iddepartamento = request.POST['departamentoid']
        municipio = request.POST['municipio']
        departamento = Departamento.objects.get(id_departamento=iddepartamento)
        nueva = Municipio(nombre_municipio = municipio, departamento_id_departamento = departamento)
        nueva.save()
        return render(request, 'municipio.html', {'municipionueva':True})

def cargarmunicipiover(request):
    if request.method == 'POST':
        municipios = Municipio.objects.order_by('id_municipio')
        return render(request, 'municipio.html',{'municipios':municipios})

def cargarmodificarmunicipio(request):
    if request.method == 'POST':
        municipios = Municipio.objects.order_by('id_municipio')
        return render(request, 'municipio.html',{'municipiosmod':municipios})

def modificarmunicipio(request):
    if request.method == 'POST':
        municipio = request.POST['municipio']
        idmunicipio = request.POST['municipiomodi']
        Municipio.objects.filter(id_municipio = idmunicipio).update(nombre_municipio = municipio)
        return render(request, 'municipio.html',{'modificado':True})

def cargareliminarmunicipio(request):
    if request.method == 'POST':
        municipios = Municipio.objects.order_by('id_municipio')
        return render(request, 'municipio.html',{'municipioeli':municipios})

def eliminarmunicipio(request):
    if request.method == 'POST':
        idmunicipio = request.POST['municipioeli']
        Municipio.objects.filter(id_municipio=idmunicipio).delete()
        eliminado = True
        return render(request, 'municipio.html', {'eliminado':eliminado})

def cargarelecciones(request):
    if request.method == 'POST':
        municipios = Municipio.objects.order_by('id_municipio')
        razas = Raza.objects.order_by('id_raza')
        generos = Genero.objects.order_by('id_genero')
        partidos = Partido.objects.order_by('id_partido')
        return render(request, 'eleccion.html',{'municipios':municipios,'razas':razas,'generos':generos,'partidos':partidos})

def nuevaelccion(request):
    if request.method == 'POST':
        idmunicipio = request.POST['municipioid']
        idraza = request.POST['razaid']
        generoid = request.POST['generoid']
        partidoid = request.POST['partidoid']
        eleccionnombre = request.POST['eleccionnombre']
        anio2 = request.POST['anio']
        analfavetos2 = request.POST['analfavetos']
        alfavetos2 = request.POST['alfavetos']
        primaria2 = request.POST['primaria']
        medio2 = request.POST['medio']
        universitario2 = request.POST['universitario']
        municipio = Municipio.objects.get(id_municipio = idmunicipio)
        raza = Raza.objects.get(id_raza = idraza)
        genero = Genero.objects.get(id_genero = generoid)
        partido = Partido.objects.get(id_partido = partidoid)
        nueva = Eleccion(nombre_eleccion = eleccionnombre, anio = anio2, analfavetos = analfavetos2, alfavetos = alfavetos2, primaria = primaria2, medio = medio2, universitario = universitario2, municipio_id_municipio = municipio, partido_id_partido = partido, genero_id_genero = genero, raza_id_raza = raza)
        nueva.save()
        return render(request, 'eleccion.html', {'eleccionnueva':True})

def cargareleccionver(request):
    if request.method == 'POST':
        elecciones = Eleccion.objects.order_by('id_eleccion')
        return render(request, 'eleccion.html', {'elecciones':elecciones})

def cargarmodificareleccion(request):
    if request.method == 'POST':
        elecciones = Eleccion.objects.order_by('id_eleccion')
        return render(request, 'eleccion.html', {'eleccionesmod':elecciones})

def modificareleccion(request):
    if request.method == 'POST':
        eleccionmodi = request.POST['eleccionmodi']
        eleccionnombre = request.POST['eleccionnombre']
        anio2 = request.POST['anio']
        analfavetos2 = request.POST['analfavetos']
        alfavetos2 = request.POST['alfavetos']
        primaria2 = request.POST['primaria']
        medio2 = request.POST['medio']
        universitario2 = request.POST['universitario']
        if eleccionnombre != "":
            Eleccion.objects.filter(id_eleccion = eleccionmodi).update(nombre_eleccion = eleccionnombre)
        if anio2 != '0':
            Eleccion.objects.filter(id_eleccion = eleccionmodi).update(anio = anio2)
        if analfavetos2 != '0':
            Eleccion.objects.filter(id_eleccion = eleccionmodi).update(analfavetos = analfavetos2)
        if alfavetos2 != '0':
            Eleccion.objects.filter(id_eleccion = eleccionmodi).update(alfavetos = alfavetos2)
        if primaria2 != '0':
            Eleccion.objects.filter(id_eleccion = eleccionmodi).update(primaria = primaria2)
        if medio2 != '0':
            Eleccion.objects.filter(id_eleccion = eleccionmodi).update(medio = medio2)
        if universitario2 != '0':
            Eleccion.objects.filter(id_eleccion = eleccionmodi).update(universitario = universitario2)
        return render(request, 'eleccion.html',{'modificado':True})

def cargareliminareleccion(request):
    if request.method == 'POST':
        eleccions = Eleccion.objects.order_by('id_eleccion')
        return render(request, 'eleccion.html',{'eleccioneli':eleccions})

def eliminareleccion(request):
    if request.method == 'POST':
        ideleccion = request.POST['eleccioneli']
        Eleccion.objects.filter(id_eleccion=ideleccion).delete()
        eliminado = True
        return render(request, 'eleccion.html', {'eliminado':eliminado})