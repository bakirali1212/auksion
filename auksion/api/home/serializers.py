from rest_framework import serializers
from ..home.models import Productmodel
class ProductListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Productmodel
        fields = "__all__"
        
        
