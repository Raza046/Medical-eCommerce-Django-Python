from django.contrib import admin
from carts.models import myCart,CartItems
# Register your models here.


class CartAdmin(admin.ModelAdmin):

    class Meta:
        model = myCart


admin.site.register(myCart,CartAdmin)

class CartItemsAdmin(admin.ModelAdmin):

    class Meta:
        model = CartItems


admin.site.register(CartItems,CartAdmin)

