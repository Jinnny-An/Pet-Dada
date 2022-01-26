from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from html5lib import serialize
from .models import Category, Store, User
from django.forms.models import model_to_dict
from django.utils import timezone
import json

def insert(request):
    # Category(c_id=1,c_name='식당').save()
    # Category(c_id=2,c_name='카페').save()
    # Category(c_id=3,c_name='병원').save()
    # Category(c_id=4,c_name='백화점').save()
    # Category(c_id=5,c_name='반려용품').save()
    # Category(c_id=6,c_name='공원').save()
    # Category(c_id=7,c_name='미용').save()
    # Category(c_id=8,c_name='숙박시설').save()

    return HttpResponse("데이터 입력 완료")

def show_main(request):
    return render(request, 'main/pet_main.html')

def show(request):
    store_list = Store.objects.filter(c_id=2)

    return render(
        request,
        'main/pet_main.html',
        {'store_list':store_list}
    )


@csrf_exempt
def ajaxGet(request):
    key = request.GET.get('key')
    print(f'key = {key}')

    store_list = Store.objects.filter(c_id=key)
    print(store_list)

    out = ''
    num = 0     # 가게별로 설명창이 열리게 설정하기 위해서 num변수 추가

    for store in store_list:
        img_path = str(store.store_img).lstrip('/main')

        out += '<div class="list-shop-content"> <div class="store_title">'
        out += store.store_name + '</div><img src="/'
        out += img_path + '" id="store-image"/><br><span>'
        out += store.store_addr + '</span><br><pre>'
        out += store.time + '</pre><span>'
        out += store.store_phone + '</span><br>'
        out += '<button class="btn-btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample'+str(num)+'" aria-expanded="false" aria-controls="collapseExample'+str(num)+'"> ▽ </button>'
        out += '<div class="collapse" id="collapseExample'+str(num)+'"> <div class="card card-body"> <pre>'
        out += store.intro + '</pre></div></div></div><hr>'

        num += 1

    # for store in store_list:
    #     img_path = str(store.store_img).replace('main/static/', '')

    #     out += '<div class="list-shop-content"> <div class="store_title">'
    #     out += store.store_name + '</div><br><img id="store-image" src="{% static ' + "'"
    #     out += img_path + "'" + ' %}" /><br><span>'
    #     out += store.store_addr + '</span><br><pre>'
    #     out += store.time + '</pre><span>'
    #     out += store.store_phone + '</span><br>'
    #     out += '<button class="btn-btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample'+str(num)+'" aria-expanded="false" aria-controls="collapseExample'+str(num)+'"> ▽ </button>'
    #     out += '<div class="collapse" id="collapseExample'+str(num)+'"> <div class="card card-body"> <pre>'
    #     out += store.intro + '</pre></div></div></div><hr>'

    #     num += 1

    return HttpResponse(out)
    # return render(request, 'main/pet_main.html', {'store_list':res})
    # return JsonResponse(res, safe=False)


@csrf_exempt
def ajaxPost(request):
    key = request.POST.get('key')
    store_list = Store.objects.filter(c_id=key)

    if request.method == 'POST':   
        print(f'key = {key}')  
        return render(request, 
            'main/pet_main.html',
            {'store_list':store_list}
            )
 
    return render(request, 'main/pet_main.html')