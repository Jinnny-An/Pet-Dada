from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from .models import Category, Store, User
from django.forms.models import model_to_dict
from django.utils import timezone

def insert(request):
    # Category(c_id=1,c_name='식당').save()
    # Category(c_id=2,c_name='카페').save()
    # Category(c_id=3,c_name='병원').save()
    # Category(c_id=4,c_name='백화점').save()
    # Category(c_id=5,c_name='반려용품').save()
    # Category(c_id=6,c_name='공원').save()
    # Category(c_id=7,c_name='미용').save()
    # Category(c_id=8,c_name='숙박시설').save()

    # Store(
    #     store_name='온사이드',
    #     store_addr='경기 남양주시 퇴계원읍 별내2로 203-11',
    #     store_phone='031-528-5399',
    #     time='매일 11:00 - 20:00 , 19:00 라스트오더',
    #     intro="★강아지입장료 소형4,000원, 중형5,000원★<br>★남아, 미중성여아 매너벨트 필수착용★<br>★노키즈존입니다 (중학생이상/부모님동반)★<br>★15kg이하 / 5차접종이상 입장가능★<br>★대형견, 진도견은 입장을 제한합니다★<br><br> - 1층 / 인조잔디, 카페 (디저트, 떡볶이, 볶음밥)<br>/ 강아지화식(닭, 소고기, 연어, 파스타)<br>- 2층 / 애견미용, 애견호텔 (예약제)<br> - 3층 / 야외루프탑 (잔디)",
    #     c_id=2
    # ).save()

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
    res = []
    
    for c in store_list:
        c = model_to_dict(c)
        res.append(c)

    print(res)

    return render(
        request,
        'main/pet_main.html',
        {'store_list':res}
    )


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