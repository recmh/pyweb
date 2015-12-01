from django.shortcuts import render,redirect
# Create your views here.

from django.http import HttpResponse
import datetime
from fafer.models import User

def month_archive(request,year,month):
    now = datetime.datetime.now()
    users = User.objects.all()
    return render(request,'user.html',{'users':users,'now':'%s' % now})

def page404(request):
    return redirect('/static/404.html')

def page500(request):
    return HttpResponse('500,server error!')
 
def page403(request):
    return HttpResponse('403,page permission denied!')

def page400(request):
    print(request)
    return HttpResponse('400,page bad request!')
