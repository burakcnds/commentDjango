from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .forms import *

from django.contrib import messages

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = UyeGirisForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            
            # Cleaned_Data djangonun sağladığı string veri çekme methodudur. .get ile beraber kullanırsak veriyi almayı başarırız.
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f'Giriş Başarılı, Hoşgeldin {request.user.first_name}')
                next_url = request.GET.get('next',None)
                # Request.get.get kodu bana urli verir
                if next_url is None:
                    return redirect('index')
                else:
                    return redirect(next_url)           
             
        else:
            messages.error(request,'Giriş Başarısız Kullanıcı Adı Veya Şifre Yanlış')
            return render(request,'login.html',{'form':form})
    form = UyeGirisForm()
    
    return render(request,'login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')


def user_register(request):
    if request.method == 'POST':
        form = UyeKayitForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('login')
        else:
            return render(request,'register.html',{'form':form})   
    form = UyeKayitForm()
    return render(request,'register.html',{'form':form})  


def sifre_degis(request):
    if request.method == 'POST':
        form = SifreDegistir(request.user,request.POST)
        if form.is_valid():

            anlikkisi = form.save()
            update_session_auth_hash(request,anlikkisi)
            messages.info(request,'Şifre Başarıyla Değiştirildi')
            return redirect('index')
        else:
            messages.error(request,'Bir Hata Yaptınız')
            return render(request,'sifreDegis.html',{'form':form})
    form = SifreDegistir(request.user)
    
    return render(request,'sifreDegis.html',{'form':form})
