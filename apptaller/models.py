

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Administrador(models.Model):
    nombreAdministrador = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return  self.nombreAdministrador

class Recepcionista(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nombreRecepcionista = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreRecepcionista

class Repuesto(models.Model):
    nombre = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class JefeAlmacen(models.Model):
    nombreJefe = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreJefe

class Tecnico(models.Model):
    nombreTecnico = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreTecnico

class Marca(models.Model):
    nombreMarca = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreMarca

class Camion(models.Model):
    placa = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return self.placa

class Conductor(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    Pedido_status = [
        (1, 'Aprobado'),
        (2, 'Por Aprobar')
    ]
    Pedido_tipoPedido = [
        (1, 'Solicitud de Permiso de Repuestos'),
        (2, 'Solicitud de Comprar Nuevos Repuestos')
    ]
    JefeAlmacen = models.ForeignKey(JefeAlmacen, on_delete=models.CASCADE)
    Tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Camion= models.ForeignKey(Camion, on_delete=models.CASCADE)
    repuesto = models.ForeignKey(Repuesto, on_delete=models.CASCADE)
    estado = models.IntegerField(null=False, blank=False, choices=Pedido_status)
    asunto = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    tipo_pedido= models.IntegerField(null=False, blank=False, choices=Pedido_tipoPedido)
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)

    def __str__(self):
        return self.asunto

class Diagnostico(models.Model):
    recepcionista = models.ForeignKey(Recepcionista, on_delete=models.CASCADE)
    Camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
    Conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)
    fecha = models.DateTimeField()
