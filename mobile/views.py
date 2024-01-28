from django.shortcuts import render, redirect ,HttpResponseRedirect
from django.http import HttpResponse
from .models import Student
from .forms import studentreg

def home(request):
    if request.method == 'POST':
        fm = studentreg(request.POST)  
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            mobile = fm.cleaned_data['mobile']
            address = fm.cleaned_data['address']
            saved = Student(name=name, email=email, password=password, mobile=mobile, address=address)
            saved.save()
            return redirect('home')
    else:
        fm = studentreg()
        data=Student.objects.all()

    return render(request, 'index.html', {'fm': fm,'data':data})


# delete a Data

def delete_data(request,id):
     pi=Student.objects.get(id=id)
     pi.delete()
     return redirect('/')
 
 
# this function will update and edit 
def update_data(request,id):
    if request.method =='POST':
        pi=Student.objects.get(id=id)
        fm=studentreg(request.POST ,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
     pi=Student.objects.get(id=id)
     fm=studentreg(instance=pi)
            
    return render(request,'update.html',{'fm':fm})




# Session Action Perform ..........

def setsession(request):
    request.session['name']='soyal'
    #request.session.set_expiry(60) #this is count the second
    return render(request,'setsession.html')


def getsession(request):
    # name = request.session['name']
    name=request.session.get('name',default='Guest')
    return render(request,'getsession.html',{'name':name})


def delsession(request):
  
    # del request.session['name']   #this is use only delete the data
    request.session.flush()  #the flush method delete all data and sessionid....
   # request.session.clear_expired() #This method use to all data clear of the database
    return render(request,'delsession.html')
