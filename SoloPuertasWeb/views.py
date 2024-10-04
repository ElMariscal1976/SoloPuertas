from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.http import HttpResponseRedirect
from .models import Producto, Tipo, Slider
from .forms import ContactoForm, SubscripcionForm
from django.conf import settings
import mercadopago
import json


# Create your views here.
def base(request):
    submitted = False
    if request.method == 'POST':
        Subscrip_form = Subscripcion_form(request.POST)
        if Subscrip_form.is_valid():
            Subscrip_form.save()
            return HttpResponseRedirect('/SoloPuertasWeb/home?submitted=True')
    else:
      Subscrip_form = Subscripcion_form()
      if 'submitted' in request.GET:
        submitted = True
    return render(request,"SoloPuertasWeb/home.html",{'Subscrip_form':Subscrip_form, 'submitted':submitted})

def resultado_busqueda(request):    
    
    if request.GET["tipo"]:
        tip_value=request.GET["tipo"]
        TipoBusqueda = Tipo.objects.filter(descripcion=tip_value)

    if request.GET["prd"]:
        prod=request.GET["prd"]
        
        if len(prod)>20:
            mensaje = "Texto de busqueda demasiado largo"
        else:
            lista_productos=Producto.objects.filter(nombre__icontains=prod, tipo__in=TipoBusqueda)
            #,tipo__exact=TipoBusqueda
            return render(request,"SoloPuertasWeb/resultado_busqueda.html",{'lista_productos':lista_productos, 'query':prod})
    else:
        mensaje="No has introducido nada"

    return HttpResponse(mensaje)

def home(request):
    slider_list = Slider.objects.all()
    lista_prod = Producto.objects.all()
    paginator = Paginator(lista_prod,2)
    pagina = request.GET.get("page") or 1
    productos = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, productos.paginator.num_pages + 1)

    return render(request,"SoloPuertasWeb/home.html",
        {"productos":productos,"paginas":paginas,"pagina_actual":pagina_actual,"slider_list":slider_list})

#def puertas(request):
#    return render(request,"SoloPuertasWeb/puertas.html")

def aluminio(request):
    return render(request,"SoloPuertasWeb/enaluminio.html")

def galeria(request):
    return render(request,"SoloPuertasWeb/galeria.html")

def contacto(request):
    submitted = False
    if request.method == 'POST':
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            contacto_form.save()
            return HttpResponseRedirect('/SoloPuertasWeb/contacto?submitted=True')
    else:
      contacto_form = ContactoForm()
      if 'submitted' in request.GET:
        submitted = True
    return render(request,"SoloPuertasWeb/contacto.html",{'formulario':contacto_form, 'submitted':submitted})

def lista_productos(request):
    TipoBusqueda = Tipo.objects.filter(descripcion='PUERTA')
    lista_prod = Producto.objects.filter(tipo__in=TipoBusqueda)  
    paginator = Paginator(lista_prod,2)
    pagina = request.GET.get("page") or 1
    productos = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, productos.paginator.num_pages + 1)
    return render(request,"SoloPuertasWeb/puertas.html",
        {"productos":productos,"paginas":paginas,"pagina_actual":pagina_actual})

def lista_aluminio(request):
    TipoBusqueda = Tipo.objects.filter(descripcion='ALUMINIO')
    lista_alum = Producto.objects.filter(tipo__in=TipoBusqueda)  
    paginator = Paginator(lista_alum,2)
    pagina = request.GET.get("page") or 1
    aluminios = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, aluminios.paginator.num_pages + 1)
    return render(request,"SoloPuertasWeb/enaluminio.html",
        {"aluminios":aluminios,"paginas":paginas,"pagina_actual":pagina_actual})

def process_payment(request):
    mp = mercadopago.MP(settings.MERCADOPAGO_CLIENT_ID,
                        settings.MERCADOPAGO_CLIENT_SECRET)

    preference = {
        'items': [
            {
                'title': 'Producto',
                'quantity': 1,
                'currency_id': 'ARS',
                'unit_price': 1000.00,
            }
        ]
    }

    preference_result = mp.create_preference(preference)
    # Redirigir al usuario a la URL del checkout generada por MercadoPago 
    return HttpResponseRedirect(preference_result['response']['init_point'])

def checkout(request):
    # Configurar las credenciales de MercadoPago
    client_id = settings.MERCADOPAGO_CLIENT_ID
    client_secret = settings.MERCADOPAGO_CLIENT_SECRET

    mp = mercadopago.MP(client_id, client_secret)
    
    # Crear preferencia con los detalles del producto
    preference_data = {
        'items': [
            {
                'title': 'Producto ejemplo',
                'quantity': 1,
                'currency_id': 'ARS',  # Reemplaza por la moneda correspondiente
                'unit_price': 100.00   # Reemplaza por el precio del producto
            }
        ]
    }    
    preference = mp.create_preference(preference_data)
    return render(request, "SoloPuertasWeb/checkout.html", {'preference': preference})