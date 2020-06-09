from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def list(request):
    return render(request,'planetlist/list.html')

def view(request):
    a=[]
    x=request.POST.copy()
    if 'csrfmiddlewaretoken' in x:
        del x['csrfmiddlewaretoken']
    if x:
        for _ in x:
            a.append(x[_])
        return render(request,'planetlist/view.html',{'list':a,'head':'Favourite Planets'})
    else:
        return render(request,'planetlist/view.html',{'list':["You haven't selected any Planet"],'head':'Favourite Planets'})
