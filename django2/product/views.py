from django.shortcuts import render

# Create your views here.
from .models import Product

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def product(request):
    productName=''
    sprice=''
    eprice=''
    
    if 'p' in request.GET:
        
        productName = request.GET['p']
        sprice = request.GET['priceS']
        eprice = request.GET['priceE']
        
        #只有產品名稱，但沒有價格範圍
        if ( len(productName) > 0 and len(sprice) == 0 and len(eprice) == 0):
            allGoods = Product.objects.filter(name__icontains=productName).order_by('-id')
        # 沒有產品名稱，但有價格範圍
        elif ( len(productName) == 0 and len(sprice) > 0 and len(eprice) > 0):
            allGoods = Product.objects.filter(price__gte=sprice,price__lte=eprice).order_by('-id')
        # 三個都有的    
        elif  ( len(productName) > 0 and len(sprice) > 0 and len(eprice) > 0 ):
            allGoods = Product.objects.filter(name__icontains=productName,price__gte=sprice,price__lte=eprice).order_by('-id')
            
        else:
            allGoods = Product.objects.all().order_by('-id')
        
    else:
        #抓取全部的資料，並以id欄位作遞減排序
        allGoods = Product.objects.all().order_by('-id')
    
    paginator = Paginator(allGoods,8)
    page = request.GET.get('page')
    try:
        allGoods = paginator.page(page)
    except PageNotAnInteger:
        allGoods = paginator.page(1)
    except EmptyPage:
        allGoods = paginator.page(paginator.num_pages)
    
    return render(request,'product.html',locals())
