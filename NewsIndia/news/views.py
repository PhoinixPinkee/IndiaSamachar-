from django.shortcuts import render
from .models import contactus,category,city,slider,news,videos,bnews
from django.http import HttpResponse
# Create your views here.
def index(request):
    data=category.objects.all().order_by('-id')[0:6]
    cnews=news.objects.all()
    citydata=city.objects.all().order_by('-id')
    sslider=slider.objects.all().order_by('id')
    mydict={"cdata":data,"ctdata":citydata,"cslider":sslider,"lnews":cnews}
    return render(request,'news/index.html',mydict)
def about(request):
    return render(request,'news/about.html')
def News(request):
    Bnews = bnews.objects.all().order_by('-id')[0:8]
    yourdict = {"bulnews":Bnews}
    return render(request,'news/News.html',yourdict)
def videonews(request):
    video=videos.objects.all().order_by('-id')[0:4]
    yourdict={"cvideos":video}
    return render(request,'news/videonews.html',yourdict)

def login(request):
    return render(request,'news/login.html')

def contact(request):
    if request.method=="POST":
        x1=request.POST.get('name')
        x2=request.POST.get('mobile')
        x3=request.POST.get('email')
        x4=request.POST.get('message')
        contactus(Name=x1,Mobile=x2,Email=x3,Message=x4).save()
        return HttpResponse("<script>alert('Thankyou For Contacting with us...');location.href='/contact/'</script>")


    #md={"Name":a,"Mobile":b,"Email":c,"Message":d}

    return render(request,'news/contact.html')