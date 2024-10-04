from django.urls import path
from SoloPuertasWeb import views

urlpatterns = [
    path('',views.home, name="Home"),
    path('puertas',views.lista_productos, name="Puertas"),
    path('aluminio',views.lista_aluminio, name="Aluminio"),
    path('galeria',views.galeria, name="Galeria"),
    path('contacto',views.contacto, name="Contacto"),
    path('checkout',views.process_payment, name="Checkout"),
    path('resultado_busqueda',views.resultado_busqueda),
    ]
