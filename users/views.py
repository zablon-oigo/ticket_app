from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterCustomerForm,LoginForm


# register a customer
def register_customer(request):
    if request.method =='POST':
        form=RegisterCustomerForm(request.POST)
        if form.is_valid():
            var=form.save(commit=False)
            var.is_customer=True
            var.save()
            messages.info(request,'Your account has been successfully registered please Log in to continue...')
            return redirect ('login')
        else:
            messages.error(request,'please correct the following error')
            return redirect('register-customer')
        
    # if request is not Post to render the form only
    else:
        form=RegisterCustomerForm()
        return render(request,'users/register_customer.html',{'form':form})

# login a customer

def login_user(request):
    if request.method =='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
        # username=request.POST.get('username')
        # password=request.POST.get('password')
            user=authenticate(request,username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                messages.info(request,'Log in sucessfully')
                return redirect('dashboard')
            messages.warning(request,'Invalid username or password')
            return redirect('login')
    else:
        
        form=LoginForm()
        return render(request,'users/login.html',{'form':form})

# logout user
def logout_user(request):
    logout(request)
    messages.info(request,'logout was successfull')
    return redirect('login')
