from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.user_profile import Userprofile
from .models.cart import Cart  # Import the Cart model BillingInformation
from .models.BillingInformation import BillingInformation
from .models.payment import Payment



class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category','image']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminUserprofile(admin.ModelAdmin):
    list_display = ['name','mobile','address']



admin.site.register(Product)
admin.site.register(Category, AdminCategory)
admin.site.register(Userprofile, AdminUserprofile)

# Register the Cart model only once

from .models import Cart, CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id',)  # Add other fields you want to display in the list view

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'cart', 'product', 'quantity') 
    # your_app_name/admin.py

from django.contrib import admin
from .models import Communityprofile  # Import the Communityprofile model

class CommunityprofileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'is_approval')  # Customize the displayed fields in the admin list view

# Register the Communityprofile model with the custom admin class
admin.site.register(Communityprofile, CommunityprofileAdmin)


class BillingInformationAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'address', 'town', 'zip_code', 'payment_status', 'amount')
    list_filter = ('payment_status', 'product')
    search_fields = ('user__username', 'name', 'town', 'zip_code')
    list_per_page = 25

admin.site.register(BillingInformation, BillingInformationAdmin)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'razorpay_order_id', 'payment_id', 'amount', 'currency', 'timestamp', 'payment_status')
    list_filter = ('payment_status',)


