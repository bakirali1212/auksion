from django.shortcuts import render
from .models import Productmodel
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import ProductListSerializers
from rest_framework.views import APIView
from rest_framework.views import Response
# Create your views here.
class ProductListView(ListAPIView):
    model = Productmodel
    queryset = Productmodel.objects.all()
    serializer_class = ProductListSerializers
    
class ProductSingleView(APIView):
    def get(self, request):
        check_data = Productmodel.objects.get(uuid=request.data["product_id"])
        data = ProductListSerializers(check_data)
        data = {
            "status" : True,
            "data" : data.data
        }
        return Response(data)
    
class CreateProductView(CreateAPIView):
    serializer_class = ProductListSerializers
    queryset = Productmodel.objects.all()