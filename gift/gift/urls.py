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
from giftapp.views import index, register, cart,about, viewproducts,detail, contact, userprofile,communityprofile, login_page,register, dashlegal,approve_certification,loggout,admin_dashboard, admin_addcategory, admin_category, community_dashboard, community_addproduct, community_product,edit_profile, community_edit_profile,admin_delete_category, admin_edit_category, community_edit_product,paymenthandler,payment,admin_view_booking
from django.conf.urls.static import static
from django.urls import path
from giftapp import views
# from giftapp.views import view_orders
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
    path('community_add_product',community_addproduct,name='community_addproduct'),
    path('community_deleteproduct//<int:product_id>/',views.community_deleteproduct,name='community_deleteproduct'),
    path('community_product',community_product,name='community_product'),
    path('admin_addcategory/',admin_addcategory,name='admin_addcategory'),
    path('admin_edit_category/<int:category_id>/', views.admin_edit_category, name='admin_edit_category'),
    path('community_product/<int:product_id>/', views.community_product, name='community_product'),
    path('community_product', views.community_product, name='community_product'),
    path('cart/', views.cart_view, name='cart_view'),
    path('community_product', views.community_product, name='community_product'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # path('view-orders/', view_orders, name='view_orders'),
    path('registered_customers/', views.registered_customer_count, name='registered_customer_count'),
    path('detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('community_edit_product/<int:product_id>/', views.community_edit_product, name='community_edit_product'),
    path('admin_delete_category/<int:category_id>/',admin_delete_category, name='admin_delete_category'),
    path('products_list/<int:category_id>/',views.products_list,name='products_list'),
    path('search_product', views.search_product, name='search_product'),
    path('admin_category/',admin_category,name='admin_category'),
    path('dashlegal', views.dashlegal, name='dashlegal'),
    path('admin_view_booking/',admin_view_booking,name='admin_view_booking'),

    path('login_page',login_page,name='login_page'),
    path('loggout',loggout,name='loggout'),
    path('register',register,name='register'),
    path('block_user/<int:user_id>/', views.block_user, name='block_user'),
    path("",include("allauth.urls")),
    path('community/add_products/', views.community_addproduct, name='community_add_products'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('approve_user/<int:user_id>/', views.approve_user, name='approve_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_base/', views.admin_base, name='admin_base'),   
    path('all-users/', views.all_users, name='all_users'),
    path('billing/<int:user_id>/', views.billing, name='billing'),
    path('payment/<int:billing_id>/', payment, name='payment'),
    path('paymenthandler/<int:billing_id>/', paymenthandler, name='paymenthandler'),
    path('approve_certification/<int:product_id>/', approve_certification, name='approve_certification'),
    path('viewproducts',viewproducts,name='viewproducts'),
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)