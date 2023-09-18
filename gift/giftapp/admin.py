from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.user_profile import Userprofile

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminUserprofile(admin.ModelAdmin):
    list_display = ['name','mobile','address']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Userprofile,AdminUserprofile)

