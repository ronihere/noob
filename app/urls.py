from django.urls import path,include
from app import views
urlpatterns = [
    path('', views.home),
    path('accounts/',include('allauth.urls'),name='accounts'),
    path('product-detail/', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    # path('login/', views.login, name='login'),
    # path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('hood/', views.hood, name='hood'),
    path('glass/', views.glass, name='glass'),
    path('shoe/', views.shoe, name='shoe'),
    path('cap/', views.cap, name='cap'),
    path('custom/',views.custom,name='custom'),
]
