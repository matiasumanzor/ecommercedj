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
    #dejar vacia la url base de esta forma nuestra vista preincipal sera store.html
    path('', views.store, name="store"),
    path('login/', views.login, name="login"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    
]