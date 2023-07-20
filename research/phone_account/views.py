from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_detail.html/')

    else:
        form = SignupForm()
    
    param = {
        'form': form
    }

    return render(request, 'signup.html', param)

def login_view(request):
    if request.method == 'POST':
        next = request.POST.get('next')
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                if next == 'None':
                 return redirect('user_detail.html/')
                else:
                    return redirect(to=next)
            

    else:
        form = LoginForm()
        next = request.GET.get('next')

    param = {
        'form': form,
        'next': next
    }

    return render(request, 'login.html', param)

@login_required
def logout_view(request):
    logout(request)
<<<<<<< HEAD

    return render(request, 'logout.html')

@login_required
def user_detail_view(request):
    #return HttpResponseRedirect(reverse('phone_account:initial.html'))
    context = {
        'user': request.user  # request.user はログインしているユーザーオブジェクトを表します
    }
    return render(request, 'user_detail.html',context)
=======
    return render(request, 'phone_account/logout.html')

@login_required
def initial_view(request):
    user = request.user
    return render(request, 'phone_account/initial.html',{'user': user})

@login_required
def test_view(request):
    return render(request, 'phone_account/test.html')
>>>>>>> 8654a54 (ノートPC（名前表示）)
