from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import p_support_Item,Other_requests,Account
from adminer.models import Bulletin_middle,Bulletin
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_detail')

    else:
        form = SignupForm()
    
    param = {
        'form': form
    }

    return render(request, 'phone/signup.html', param)

def login_view(request):
    if request.method == 'POST':
        next = request.POST.get('next')
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                if next == 'None':
                 return redirect('user_detail')
                else:
                    return redirect(to=next)
            

    else:
        form = LoginForm()
        next = request.GET.get('next')

    param = {
        'form': form,
        'next': next
    }

    return render(request, 'phone/login.html', param)

@login_required
def logout_view(request):
    logout(request)

    return render(request, 'phone/logout.html')

@login_required
def user_detail_view(request):
    context = {
        'user': request.user
    }
    return render(request, 'phone/user_detail.html',context)

@login_required
def supplies_view(request):
    if request.method == 'POST':
        item_name = ''

        selectedCategory = request.POST.get('category', None)
        if selectedCategory:
            item_name += selectedCategory

            selectedSubCategory1 = request.POST.get('subCategory', None)
            itemDetails = request.POST.get('itemDetails', None)
            if selectedSubCategory1:
                item_name += ' ' + selectedSubCategory1
            elif itemDetails:
                item_name += ' ' + itemDetails
            
                selectedSubCategory2 = request.POST.get('subSubCategory', None)
                itemDetails = request.POST.get('itemDetailsText', None)
                if selectedSubCategory2:
                    item_name += ' ' + selectedSubCategory2
                elif itemDetails:
                    item_name += ' ' + itemDetails

                    selectedSubCategory3 = request.POST.get('sub3Category', None)
                    if selectedSubCategory3:
                        item_name += ' ' + selectedSubCategory3

                        selectedSubCategory4 = request.POST.get('clothingCategory', None)
                        itemDetails2 = request.POST.get('itemDetails-2', None)
                        if selectedSubCategory4:
                            item_name += ' ' + selectedSubCategory4
                        elif itemDetails2:
                            item_name += ' ' + itemDetails2
        quantity = request.POST.get('quantity', 0)
        account_id = request.user.id
        p_support_Item.objects.create(item_name=item_name, quantity=quantity, account_id=account_id)
        return redirect('p_success')

    return render(request, 'phone/supplies.html')

@login_required
def p_success_view(request):
    return render(request, 'phone/p_success.html')

@login_required
def base_view(request):
    return render(request, 'phone/base.html')

@login_required
def history_view(request):
    user_support_items = p_support_Item.objects.filter (account_id = request.user.id)
    context = {
        'history': user_support_items
    }
    return render(request, 'phone/history.html',context)

@login_required
def p_requests_view(request):
    if request.method == 'POST':
        request_text = request.POST.get('requests', None)
        account_id = request.user.id
        Other_requests.objects.create(requests=request_text, account_id=account_id)
        return redirect('p_success')
    return render(request, 'phone/p_requests.html')

@login_required
def edit_basic_info(request):
    user =request.user
    if request.method == 'POST':
        form = SignupForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('p_success')
    else:
        form =SignupForm(instance=user)
    param = {
        'form':form
    }
    return render(request,'phone/edit_basic_info.html',param)

@login_required
def response_view(request):
    # ログイン中の避難者のIDを取得
    account_id = request.user.id
    # 避難者が登録している避難所のIDを取得
    shelter_id = Account.objects.get(id=account_id).shelter_id
    # メッセージをテンプレートに渡す
    notice_text = Bulletin_middle.objects.filter(shelter_id=shelter_id).select_related('bulletin')
    print(notice_text) 
    context = {
        'notice_text': notice_text,
    }
    return render(request, 'phone/response.html', context)
