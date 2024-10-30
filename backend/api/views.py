from django.http import JsonResponse,HttpResponse
from product.models import Products
import json
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.serializer import ProductSerializer
# Create your views here.

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    # instance = Products.objects.order_by("?").first()
    # if instance:
    #     data = ProductSerializer(instance).data

    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        # print(serializer.data)
        data = serializer.data
        return Response(data)
    return Response({'invalid':"not a valid data"}, status=400)
    