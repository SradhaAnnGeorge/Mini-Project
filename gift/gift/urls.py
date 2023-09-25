"""
URL configuration for gift project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from giftapp.views import index, register, cart,about, detail, contact, userprofile,communityprofile, login_page,register,loggout,admin_dashboard,admin_product, admin_addproduct, admin_addcategory, admin_category, community_dashboard, community_addproduct, community_product,edit_profile, community_edit_profile,admin_delete_category, admin_edit_category, community_edit_product, admin_dashboard_cards
from django.conf.urls.static import static
from django.urls import path
from giftapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # path('loginn', loginn, name='loginn'),
    # path('register', register, name='register'),
    path('cart',cart, name='cart'),
    path('about',about, name='about'),
    path('contact',contact, name='contact'),
    path('detail',detail,name='detail'),
    path('userprofile/',userprofile, name='userprofile'),
    path('editprofile/',edit_profile, name='edit-profile'),
    path('communityprofile/',communityprofile, name='communityprofile'),
    path('communityeditprofile/',community_edit_profile, name='communityedit-profile'),
    path('admin_dashboard/',admin_dashboard,name='admin_dashboard'),
    path('community_dashboard/',community_dashboard,name='community_dashboard'),
    path('admin_addproduct/',admin_addproduct,name='admin_addproduct'),
    path('community_add_product',community_addproduct,name='community_addproduct'),
    path('community_deleteproduct//<int:product_id>/',views.community_deleteproduct,name='community_deleteproduct'),
    path('admin_product/',admin_product,name='admin_product'),
    path('community_product',community_product,name='community_product'),
    path('admin_addcategory/',admin_addcategory,name='admin_addcategory'),
    # path('admin_edit_category/', admin_edit_category, name='admin_edit_category'),
    path('admin_edit_category/<int:category_id>/', views.admin_edit_category, name='admin_edit_category'),
    path('admin_dashboard_cards/', admin_dashboard_cards, name='admin_dashboard_cards'),
    path('community_product/<int:product_id>/', views.community_product, name='community_product'),
    path('community_product', views.community_product, name='community_product'),
    path('cart/', views.cart_view, name='cart_view'),
    path('community_product', views.community_product, name='community_product'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('registered_customers/', views.registered_customer_count, name='registered_customer_count'),
    path('detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('community_edit_product/<int:product_id>/', views.community_edit_product, name='community_edit_product'),
    path('admin_delete_category/<int:category_id>/',admin_delete_category, name='admin_delete_category'),
    path('products_list/<int:category_id>/',views.products_list,name='products_list'),
    
    path('admin_category/',admin_category,name='admin_category'),
    path('login_page',login_page,name='login_page'),
    path('loggout',loggout,name='loggout'),
    path('register',register,name='register'),
    path("",include("allauth.urls")),
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)