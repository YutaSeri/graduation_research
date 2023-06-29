from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/phone_account/initial/')

    else:
        form = SignupForm()
    
    param = {
        'form': form
    }

    return render(request, 'phone_account/signup.html', param)

def login_view(request):
    if request.method == 'POST':
        next = request.POST.get('next')
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                if next == 'None':
                 return redirect('/phone_account/initial/')
                else:
                    return redirect(to=next)
            

    else:
        form = LoginForm()
        next = request.GET.get('next')

    param = {
        'form': form,
        'next': next
    }

    return render(request, 'phone_account/login.html', param)

@login_required
def logout_view(request):
    logout(request)

    return render(request, 'phone_account/logout.html')

@login_required
def initial_view(request):
    return render(request, 'phone_account/initial.html')