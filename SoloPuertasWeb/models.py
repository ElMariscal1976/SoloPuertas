from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural='Proveedores'

class Clasificacion(models.Model):
    descripcion=models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural='Clasificaciones'

class Tipo(models.Model):
    descripcion=models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    clasificacion=models.ForeignKey(Clasificacion, on_delete=models.CASCADE)
    tipo=models.ForeignKey(Tipo, on_delete=models.CASCADE)
    proveedor=models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    precio=models.FloatField()
    imagen=models.ImageField(upload_to="productos", null=True, blank=True)
    observaciones=models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    nombre=models.CharField(max_length=150, verbose_name="Nombre y Apellido")
    email=models.EmailField(verbose_name="Correo Electrónico")
    mensaje=models.TextField()
    telefono=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Subscripcion(models.Model):
    email=models.EmailField(verbose_name="Correo Electrónico")
    class Meta:
        verbose_name_plural='Subscripciones'


class Slider(models.Model):
    imagen=models.ImageField(upload_to="slider", null=True, blank=True)
    
    def __str__(self):
        return 'Imagen'