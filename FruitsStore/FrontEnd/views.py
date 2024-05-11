from django.shortcuts import render,redirect

from FrontEnd.models import logindb, contactdb, cartdb
from NewApp.models import catdetail, catdata


# Create your views here.
def home(request):
    data = catdetail.objects.all()
    return render(request,'frontHome.html',{'data':data})

def filterproduct(request, cat):
    data = catdata.objects.filter(cat_name=cat)
    return render(request, 'filterproduct.html', {'data': data})


def singleproduct(request, data):
    data = catdata.objects.get(id=data)
    return render(request, 'singleproductpage.html', {'data': data})

def productpage(request):
    pro = catdata.objects.all()
    return render(request,'productpage.html', {'pro': pro})

def signuppage(request):
    return render(request, 'loginpage.html')

def savelog(request):
    if request.method == 'POST':
        a = request.POST.get('na')
        b = request.POST.get('use')
        c = request.POST.get('pass')
        obj = logindb(s_name=a, s_user=b, s_pass=c)
        obj.save()
        return redirect(signuppage)

def loginpage(request):
    return render(request, 'loginpage.html')

def loginsave(request):
    if request.method == "POST":
        d = request.POST.get('lna')
        e = request.POST.get('lpass')
        if logindb.objects.filter(s_user=d,s_pass=e).exists():
            return redirect(home)
        else:
            return redirect(loginpage)
    else:
        return redirect(loginpage)


def contact(request):
    return render(request, 'contactpage.html')

def contactdata(request):
    if request.method == 'POST':
        f = request.POST.get('nam')
        g = request.POST.get('eml')
        h = request.POST.get('sub')
        i = request.POST.get('mess')
        obj = contactdb(c_name=f, c_email=g, c_subject=h, c_message=i)
        obj.save()
        return redirect(contact)

def cart(request):
    cat = cartdb.objects.all()
    return render(request,'cart.html',{'cat':cat})

def cartdata(request):
    if request.method == 'POST':

        k = request.POST.get('nam')
        l = request.POST.get('pri')
        m = request.POST.get('qt')
        n = request.POST.get('total')
        obj = cartdb(ca_name=k,ca_price=l,ca_qty=m,ca_total=n)
        obj.save()
        return redirect(cart)

