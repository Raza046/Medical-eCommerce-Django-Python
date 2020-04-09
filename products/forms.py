from django import forms

from products.models import Products


class ProductForm(forms.ModelForm):

    class Meta:
        model = Products

        fields = [

            'quantity'
        ]


