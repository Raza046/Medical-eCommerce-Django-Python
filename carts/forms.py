from django import forms

from carts.models import CartItems


class CartItemsForm(forms.ModelForm):

    class Meta:
        model = CartItems

        fields = [

            'quantity'
        ]


