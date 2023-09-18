from django import forms
from .models import Category, Product

class CategoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['names']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Category.objects.filter(name=name).exists():
            self.add_error('name', 'Category with this name already exists.')
        return name

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'product_image']
