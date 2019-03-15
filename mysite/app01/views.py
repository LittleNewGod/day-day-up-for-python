from django.shortcuts import render
import pymysql
from app01 import models
from common.page import Pagination

# Create your views here.

def index(request):

    # 从URL中取当前访问的页码数
    current_page = int(request.GET.get('page',1))
    # 比len(models.Publisher.objects.all())更高效
    total_count = models.Product.objects.count()
    page_obj = Pagination(current_page, total_count, request.path_info)
    data = models.Product.objects.all()[page_obj.start:page_obj.end]
    page_html = page_obj.page_html()

    return render(request, 'index.html',{"data": data, "page_html": page_html})

def detail(request):

    #asin = request.GET.get('Asin','B07GRSY8RG')
    #因为详细表只有一份数据，所以这里写死了，所有目录都跳到这一份详细
    asin = 'B07GRSY8RG'
    detail_data = models.Detail.objects.filter(Asin_detail=asin).all()
    return render(request,'detail.html',{'detail_data':detail_data})
