from django.shortcuts import render, HttpResponse
from . models import Restaurant_infoModel
from django.core.paginator import Paginator
from parse import get_data_from_elements, collect_url
# Create your views here.


def index(request):
    return render(request, 'dataApp/index.html')


def kfc_data(request):
    return render(request, 'dataApp/kfc.html')


def restaurant_data_list(request):
    # urls = collect_url()
    # content = get_data_from_elements(urls)
    obj = Restaurant_infoModel.objects.all()
    paginator = Paginator(obj, 15)
    page_number = request.GET.get('page', 1) # default=1
    page = paginator.get_page(page_number)

    # logic for buttons "Next" and "Previous"
    is_paginated = page.has_other_pages() # True/False
    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''
    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''
    context = {
        'obj': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }


    return render(request, 'dataApp/restaurant.html', context=context) # object_list returned QuerySet


