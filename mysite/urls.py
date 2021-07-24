
from django.contrib import admin
from django.urls import path, include 
from mainweb import views as mw 
from cart import views as cr  
from checkout import views as ck 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('cart/', cr.view_cart , name = "cart"),  
    path('', mw.home , name = "home" ), 
    path('products/' , mw.detail , name= "Product Details" ), 
    path('checkout1/', ck.view_checkout  , name="checkout" ),
    path('twowheel/', mw.twowheeler  , name="twowheeler" ),   
 ]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT) 


