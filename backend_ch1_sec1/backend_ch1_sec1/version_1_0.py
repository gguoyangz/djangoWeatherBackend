from django.urls import path, include

urlpatterns = [
    path('service/', include('apis.urls'))
]