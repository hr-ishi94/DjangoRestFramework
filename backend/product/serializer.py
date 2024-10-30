from rest_framework import serializers
from product.models import Products

class ProductSerializer(serializers.ModelSerializer):
    my_amount = serializers.SerializerMethodField(read_only= True)
    class Meta:
        model = Products
        fields = [
            'id',
            'name',
            'price',
            'content',
            'sale_price',
            'my_amount'
            ]
        
    def get_my_amount(self,obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj, Products):
            return None
        return obj.other_amount()