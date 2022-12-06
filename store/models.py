from django.db import models
from django.contrib.auth.models import User

#Creacion  modelo tablas


# Tabla clientes:
#  user  = nombre de usuario
#  name  = Nombre real 
#  email = Direccion de correo
class Customer(models.Model):
    user             =  models.OneToOneField  (User, on_delete=models.CASCADE, null=True, blank=True)
    name             =  models.CharField      (max_length=200, null=True)
    email            =  models.CharField      (max_length=200, null=True)

    def __str__(self):
        return self.name

# Tabla productos
# name = Nombre producto
# price = Precio
# image = Imangen (se agrega desde dentro del administrador)
class Product(models.Model):
    name             =  models.CharField       (max_length=200, null=True)
    price            =  models.FloatField      ()
    digital          =  models.BooleanField    (default=False,null=True, blank=True)
    image            =  models.ImageField      (null=True, blank=True)

    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer         =  models.ForeignKey      (Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_orderd      =  models.DateTimeField   (auto_now_add=True)
    complete         =  models.BooleanField    (default=False, null=True, blank=False)
    transaction_id   =  models.CharField       (max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    #Creacion metodo de verificacion para el pedido
    @property
    def shipping(self):
        shipping = False
        OrderItems = self.orderitem_set.all()
        for i in OrderItems:
            if i.product.digital == False:
                shipping = True
        return shipping


    #Este fragmento se utiliza para el calculo dentro del carrito de compras
    #Captura las variables deseadas para posterior ser utilizadas para definir el total de la compra
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.qunatity for item in orderitems])
        return total


# Tabla de pedidos
#   product    = Nombre producto
#   order      = N° orden
#   qunatity   = Cantidad
#   date_added = Fecha
class OrderItem(models.Model):
    product          =  models.ForeignKey      (Product, on_delete=models.SET_NULL, blank=True, null=True)
    order            =  models.ForeignKey      (Order, on_delete=models.SET_NULL, blank=True, null=True)
    qunatity         =  models.IntegerField    (default=0, null=True, blank=True)
    date_added       =  models.DateTimeField   (auto_now_add=True)


    #Calculo precio lote de productos agregados al carrito
    #Toma el precio del producto y lo multiplica por la cantidad deseada
    @property
    def get_total(self):
        total = self.product.price * self.qunatity
        return total


# Tabla de direccion comprador
#   customer   = Cliente 
#   order      = N° de orden
#   address    = Direccion comprador 
#   city       = Ciudad comprador
#   state      = Comuna 
#   zipcode    = Codigo postal
#   date_added = Fecha
class ShippingAddress(models.Model):
    customer         =  models.ForeignKey      (Customer, on_delete=models.SET_NULL,blank=True, null=True)
    order            =  models.ForeignKey      (Order, on_delete=models.SET_NULL, blank=True, null=True)
    address          =  models.CharField       (max_length=200, null=True)
    city             =  models.CharField       (max_length=200, null=True)
    state            =  models.CharField       (max_length=200, null=True)
    zipcode          =  models.CharField       (max_length=200, null=True)
    date_added       =  models.DateTimeField   (auto_now_add=True)
    
    def __str__(self):
        return self.name
