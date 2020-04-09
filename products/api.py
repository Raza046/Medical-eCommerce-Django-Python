from rest_framework.views import APIView
from rest_framework.response import Response
from products.serializers import *
from .models import Products


class ProductView(APIView):

    def get(self, request):

        model = Products.objects.all()
        serializer = ProductSerializer(model ,many=True)

        return Response(serializer.data)

