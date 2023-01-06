from django.shortcuts import render

# Create your views here.
from .models import Hotel
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
def hotel(request):
    items=''
    keyword=''
    
    if 'p' in request.GET:
        
        items= request.GET['item']#下拉式選項
        keyword = request.GET['p']#關鍵字查詢
        
        if (len(keyword)>0 and len(items)==1):
            allHotel = Hotel.objects.filter(title__icontains=keyword).order_by('-id')
        elif (len(keyword)==0 and len(items)>0):
            allHotel = Hotel.objects.filter(number=items).order_by('-id')
        elif (len(keyword)>0 and len(items)>0):
            allHotel = Hotel.objects.filter(title__icontains=keyword,number=items).order_by('-id')
        else:
            allHotel =Hotel.objects.all().order_by('-id')
    else:
        allHotel =Hotel.objects.all().order_by('-id')
    paginator = Paginator(allHotel,20)
    page = request.GET.get('page')
    try:
        allHotel = paginator.page(page)
    except PageNotAnInteger:
        allHotel = paginator.page(1)
    except EmptyPage:
        allHotel = paginator.page(paginator.num_pages)
    
    return render(request,'hotel.html',locals())