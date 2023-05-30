from django.shortcuts import render,redirect
import os
from eventapp.models import event,category,myfunction,Order
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    eve=event.objects.all()
    return render(request,"index.html",{'eve':eve})

def adminindex(request):
    return render(request,'adminindex.html')

def store(request):
    return render(request,'addcategory.html')

def contact(request):
    return render(request,'contact.html')    

def addcategory(request):
    if request.method=='POST':
        categoryname=request.POST['categoryname']
        data=category(categoryname=categoryname)
        data.save()
        return redirect('addcategory')
    return render(request,'addcategory.html')

def addevent(request):
    cat=category.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        amount=request.POST['amount']
        description=request.POST['description']
        if request.FILES.get('file') is not None:
            image = request.FILES['file']
        else:
            image = "/static/image/default.png"

        cx=event.object.filter(name=name)
        if len(cx)>=1:
            return render(request,'addevent.html',{'cat':cat})        
        catgp=request.POST['sel']
        categ=category.objects.get(id=catgp)
        ctg= event(category=categ,image=image,description=description,amount=amount,name=name)
        
        ctg.save()
        return redirect('addevent')
    return render(request,'addevent.html',{'cat':cat})

def showevent(request):
    eve=event.objects.all()
    return render(request,'showevent.html',{'eve':eve})

def editdetails(request,pk):
    eve=event.objects.get(id=pk)
    cat=category.objects.all()
    context={'eve':eve,'cat':cat}
    if request.method=='POST':
        eve.name=request.POST['name']
        eve.amount=request.POST['amount']
        eve.description=request.POST['description']
        if request.FILES.get('file') is not None:
            if not eve.image == "/static/image/default.jpg":
                os.remove(eve.image.path)
                eve.image = request.FILES['file']
            else:
                eve.image = request.FILES['file']
        else:
            if eve.image=="":
                os.remove(eve.image.path)
                eve.image = "/static/image/default.jpg" 
        c=request.POST['sel']
        eve.category=category.objects.get(id=c)
        eve.save()
        return redirect('showevent')
    return render(request,'edit.html',context)

def deletedetails(request,pk):
    std=event.objects.get(id=pk)
    std.delete()
    return redirect('showevent')

def logout(request):
    auth.logout(request) 
    eve=event.objects.all()
    return render(request,'index.html',{'eve':eve}) 

def loginpage(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        address=request.POST['address']
        contact=request.POST['contact']
        if password==cpassword:
            if User.objects.filter(username=username):
                messages.info('this user is already exists')
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password)
               
                user.save()
                return render(request,'login.html')
        else:
            messages.info(request,'password doesnot match')
            return redirect('signup')
        return redirect('loginpage')
    else:
          return render(request,'register.html') 

def login_user(request):
    if request.method=='POST':
        eve=event.objects.all()
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
         # request.session["uid"]=user.id
        if user is not None:
            if user.is_staff:
                auth.login(request,user)
                return render(request,'adminindex.html') 
            else:
                 # login(request,user)
                auth.login(request,user)
                messages.info(request,f'Welcome {username}')
                return render(request,'index.html',{'eve':eve,'user':user})
                # return redirect('userhomepage')
        else:
            messages.info("invalid username or password")
            return redirect('login') 
    else:
        return render(request,'login.html')

def eventitem(request,pk,k):
    eventobj=event(id=pk)
    userobj=User(id=k)
    t=myfunction(event=eventobj,user=userobj)
    t.save()
    return redirect('index')

def loadeventitems(request,pk):
    e=myfunction.objects.filter(user=pk)
    return render(request,'event.html',{'eventitems':e})

def details(request,pk,k):
    eve=event.objects.get(id=pk)
    
    return render(request,'details.html',{'eve':eve,'u':k}) 

def profile(request,pk):
    std=User.objects.get(id=pk) 
    return render(request,'profile.html',{'std':std}) 

def showuser(request):
    std=User.objects.filter(is_staff=0)
  
    return render(request,'showuser.html',{'std':std})

def deleteuser(request,pk):
    std=User.objects.get(id=pk) 
    std.delete()
    return redirect('showuser') 

def eventitems(request):
    item=myfunction.objects.all()
    return render(request,'eventitem.html',{'item':item}) 

def deleteitem(request,pk):
    item=myfunction.objects.get(id=pk)
    item.delete()
    return redirect('eventitems')                        










        


