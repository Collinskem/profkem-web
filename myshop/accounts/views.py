from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout



def signup_view(request):
    if request.method=='POST':
     formm = UserCreationForm(request.POST)
     if formm.is_valid():
        user= formm.save()
         #login the User
        login(request,user)
        return redirect('shop:index')
    else:
        formm=UserCreationForm()
    return render(request,'accounts/signup.html',{'formm':formm})


def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login the User
          user=form.get_user()
          login(request,user)
          if 'next' in request.POST:
           return redirect(request.POST.get('next'))
          else:
            return redirect( "shop:index" )
    else:
      form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
    return redirect("shop:index")


def password_reset_done(request):
    return render(request,'accounts/password_reset_done.html')

def password_reset_confirm(request):
    return render(request,'accounts,password_reset_confirm.html')    
