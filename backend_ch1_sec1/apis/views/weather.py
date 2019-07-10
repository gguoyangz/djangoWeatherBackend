from django.http import HttpResponse, JsonResponse, FileResponse
from thirdparty import juhe
import json

def helloworld(request):
    print('request method: ', request.method)  # 请求方式
    print('request META: ', request.META)  # 请求客户端信息
    print('request cookie: ', request.COOKIES)  # 请求cookie
    print('request QueryDict: ', request.GET)  # 请求参数
    # return HttpResponse(content='hello django response', status=201)

    # 通过JsonResponse
    m = {
        'message': 'hello json response'
    }
    return JsonResponse(data=m, safe=False, status=200) # safe为false则不会检查对象，直接转换为json，设置为true则只能转换为py的字典对象

def weather(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        data = juhe.weather(city)
        return JsonResponse(data=data, status=200)
    elif request.method == 'POST':
        received_body = request.body
        received_body = json.loads(received_body)
        cities = received_body.get('cities')
        response_data = []
        for city in cities:
            result = juhe.weather(city)
            result['city'] = city
            response_data.append(result)
        return JsonResponse(data=response_data, safe=False, status=200)
