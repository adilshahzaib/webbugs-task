from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from .models import Supplier
from .models import Shop
from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


from rest_framework.decorators import api_view
from rest_framework.response import Response

 



@api_view(['GET'])
def topsupplier(request):
    suppliers = Supplier.objects.annotate(num_shops=models.Count('shops')).order_by('-num_shops')[:3]
    result = []
    for supplier in suppliers:
        shops = supplier.shops.all()
        shop_names = [{'Shop_name': shop.name} for shop in shops]
        supplier_info = {
            'Supplier Name': supplier.name,
            'Address': supplier.address,
            'Shops_detail': shop_names
        }
        result.append({'supplier_info': supplier_info})
        print('rsult',result)
    return Response(result)


@api_view(['GET'])

def searchshops(request):
     query = request.GET.get('query')
     if query:
        shops = Shop.objects.filter(name__icontains=query)
        result = [{'Shop_name': shop.name} for shop in shops]
        return Response(result)
     return Response({'error': 'Nothing found'})

@api_view(['GET'])
def shopsuppliers(request):
    shop_id = request.GET.get('shop_id')
    
    if shop_id:
        try:
            shop = Shop.objects.get(id=shop_id)
        except Shop.DoesNotExist:
            return Response({'error': 'Shop not found'})
        suppliers = shop.suppliers.all()
        result = [{'Supplier Name': supplier.name, 'Address': supplier.address} for supplier in suppliers]
        return Response(result)
    return Response({'error': 'No Shop id  found'})


@api_view(['POST'])
def ReportSend(request):
    shop_id = request.data.get('shop_id')
    if shop_id:
        try:
            shop = Shop.objects.get(id=shop_id)
        except Shop.DoesNotExist:
            return Response({'error': 'Shop not found'})
        suppliers = shop.suppliers.all()
        html_content = render_to_string('email/report.html', {'shop': shop, 'suppliers': suppliers})
        send_mail(
            'Supplier Report for {}'.format(shop.name),
            '',
            settings.EMAIL_HOST_USER,
            [request.user.email],
            #print([request.user.email])
            fail_silently=False,
            html_message=html_content
        )
        return Response({'success': True})
    return Response({'error': 'No shop found'})
