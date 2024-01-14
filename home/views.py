from django.shortcuts import render
from . models import Services
# Create your views here.

def service_list(request):
    service_list = Services.objects.all()
    context = {'services' : service_list}
    return render(request,'home/service_list.html',context)


# def service_detail(request , id):
#     pass
