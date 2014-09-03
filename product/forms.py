from django.forms import forms, ModelForm
from .models import Product


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ('price', 'image', 'name','duration','onstack')
