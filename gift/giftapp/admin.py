from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.user_profile import Userprofile
from .models.cart import Cart  # Import the Cart model

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