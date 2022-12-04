from django.urls import path
from . import views

#<!-- 
#    Main.html  → Plantilla de la que todos heredarán
#    Store.html  → Página de inicio/fachada de la tienda con todos los productos
#    Cart.html  → Carrito de compras de los usuarios
#    Checkout.html  → Página de pago 
#-->

# recuerda que main no se referencia porque es la plantilla base para todas 


urlpatterns = [
    #dejar vacia la url base
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout")
]