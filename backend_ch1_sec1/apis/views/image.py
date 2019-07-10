import os
from django.http import Http404, HttpResponse, FileResponse
from backend_ch1_sec1 import settings


def iamge(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + ',jpg')
        if not os.path.exists(imgfile):
            return Http404()
        else:
            data = open(imgfile, 'rb').read()
            return HttpResponse(content=data)
    pass