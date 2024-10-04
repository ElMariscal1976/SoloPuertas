from django.contrib import admin

# Register your models here.
from SoloPuertasWeb.models import Proveedor, Producto, Clasificacion, Tipo, Contacto, Subscripcion, Slider

class ProductoAdmin(admin.ModelAdmin):
    list_display=("nombre","clasificacion","tipo")
    search_fields=("nombre","clasificacion","tipo")
    list_filter=("clasificacion","tipo")

class ContactoAdmin(admin.ModelAdmin):
    list_display=("nombre","email","telefono")

admin.site.register(Proveedor)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Clasificacion)
admin.site.register(Tipo)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Subscripcion)
admin.site.register(Slider)

