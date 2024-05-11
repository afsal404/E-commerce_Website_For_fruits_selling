from django.shortcuts import render,redirect

from FrontEnd.models import contactdb
from NewApp.models import catdata, catdetail
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
# from django.contrib.auth.models import User

from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def demo(request):
    return render(request, 'index.html')

def regis(request):
    data = catdetail.objects.all()
    return render(request, 'register.html', {'data': data})

def tabledata(request):
    if request.method == 'POST':
        a = request.POST.get('category')
        b = request.POST.get('dec')
        c = request.POST.get('quan')
        d = request.POST.get('price')
        e = request.FILES['Img']
        obj = catdata(cat_name=a, cat_dec=b, cat_quan=c,cat_price=d, images=e)
        obj.save()
        return redirect(regis)

def table(request):
    data = catdata.objects.all()
    return render(request,'table.html', {'data': data})


def edits(request, dataid):
    details = catdata.objects.get(id=dataid)
    return render(request,'editpage.html',{'details': details})

def updateedit(request, up):
    up = catdetail.objects.get(id=up)
    return render(request,'cateedit.html',{'up':up})

def delete(request,to):
    data = catdata.objects.filter(id=to)
    data.delete()
    return redirect(table)

def update(request,dataid):
    if request.method == 'POST':
        f = request.POST.get('name')
        g = request.POST.get('dec')
        h = request.POST.get('quan')
        i = request.POST.get('price')
        catdata.objects.filter(id=dataid).update(cat_name=f, cat_dec=g, cat_quan=h,cat_price=i)
        return redirect(table)

def addproducts(request):
    cat = catdata.objects.all()
    return render(request, 'register.html', {'cat': cat})

def category(request):
    return render(request,'category.html')

def newcate(request):
    if request.method == 'POST':
        j = request.POST.get('nam')
        k = request.POST.get('de')
        l = request.FILES['Im']
        obj = catdetail(cate_nam=j,cate_de=k,image=l)
        obj.save()
        messages.success(request,'category saved successfully')
        return redirect(category)


def catable(request):
    cat = catdetail.objects.all()
    return render(request,'catetable.html',{'cat':cat})


def deletedetail(request,dataid):
    data = catdetail.objects.filter(id=dataid)
    data.delete()
    return redirect(catable)

def editupdate(request, do):
    if request.method == 'POST':
        j = request.POST.get('nam')
        k = request.POST.get('de')
        try:
            l = request.FILES['Im']
            fs = FileSystemStorage()
            file = fs.save(l.name,l)
        except MultiValueDictKeyError:
            file = catdetail.objects.get(id=do).image
        catdetail.objects.filter(id=do).update(cate_nam=j,cate_de=k,image=file)
        return redirect(catable)

def contacttable(request):
    do = contactdb.objects.all()
    return render(request,'contacttable.html', {'do':do})