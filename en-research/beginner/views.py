from django.shortcuts import render, redirect
from .forms import SearchForm
from .models import beginner_account_and_item
from .models import biginner_account_and_Other_requests
from phone.models import Shelter
import time
from django.db.models import Q

def home_view(request):
    return render(request, 'beginner/home.html')

def success_view(request):
    return render(request, 'beginner/success.html')

def requests1_view(request):
    shelters = Shelter.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        shelter_id = request.POST.get('shelter')
        
        if username and shelter_id:
            request.session['username'] = username
            request.session['shelter_id'] = shelter_id
            return redirect('requests2')
    
    return render(request, 'beginner/requests1.html', {'shelters': shelters})

def requests2_view(request):
    if request.method == 'POST':
        username = request.session.get('username')
        shelter_id = request.session.get('shelter_id')
        request_text = request.POST.get('requests')
        
        if username and shelter_id and request_text:
            shelter = Shelter.objects.get(pk=shelter_id)
            request_obj = biginner_account_and_Other_requests.objects.create(username=username, shelter=shelter, requests=request_text)
            del request.session['username']
            del request.session['shelter_id']
            
            return redirect('success')
    
    return render(request, 'beginner/requests2.html')


def search_results_view(request):
    username = request.GET.get('q', '')
    birthdate = request.GET.get('birthdate', '')
    results = beginner_account_and_item.objects.filter(
        Q(username=username) & Q(birthdate=birthdate)
    )
    return render(request, 'beginner/search_results.html', {'results': results, 'username': username, 'birthdate': birthdate})

def search_view(request):
    return render(request, 'beginner/search.html')

def supplie1_view(request):
    username = ''
    gender = ''
    birthdate = ''
    shelter_id = ''
    shelters = Shelter.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        birthdate = request.POST.get('birthdate')
        shelter_id = request.POST.get('shelter')
        item_name = ''
        if username and gender and birthdate and shelter_id:
            request.session['username'] = username
            request.session['gender'] = gender
            request.session['birthdate'] = birthdate
            request.session['shelter_id'] = shelter_id
            return redirect('supplie2')
            
    return render(request, 'beginner/supplie1.html', {'shelters': shelters})

def supplie2_view(request):
    if request.method == 'POST':
        request.session['categories'] = []
        category = request.POST.get('category')
        request.session['categories'].append(category)
       
        if category == '医療・介護用品':
            return redirect('supplie_medical')
        elif category == '食料品':
            return redirect('supplie_grocery')
        elif category == '幼児用品':
            return redirect('supplie_baby')
        elif category == 'その他':
            return redirect('supplie_other')
    return render(request, 'beginner/supplie2.html')

def supplie_medical_view(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        categories = request.session.get('categories', [])
        categories.append(category)
        request.session['categories'] = categories

        if category == '松葉杖':
            return redirect('supplie_medical_crutch')
        elif category == '車椅子':
            return redirect('supplie_medical_wheelchair')
        elif category == '歩行器':
            return redirect('supplie_medical_walker')
        elif category == '大人用おむつ':
            return redirect('supplie_medical_adult_diapers')
    return render(request, 'beginner/supplie_medical.html')

def supplie_grocery_view(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        categories = request.session.get('categories', [])
        categories.append(category)
        request.session['categories'] = categories
        
        if category:
            return redirect('confirm')
    return render(request, 'beginner/supplie_grocery.html')

def supplie_baby_view(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        categories = request.session.get('categories', [])
        categories.append(category)
        request.session['categories'] = categories
        
        if category:
            return redirect('confirm')
    return render(request, 'beginner/supplie_baby.html')

def supplie_other_view(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        categories = request.session.get('categories', [])
        categories.append(category)
        request.session['categories'] = categories

        if category == '衣服品':
            return redirect('supplie_other_clothes')
        elif category == '靴':
            return redirect('supplie_other_shoes')
        elif category == 'トイレットペーパー':
            return redirect('confirm')
        elif category == '毛布':
            return redirect('confirm')
        elif category == '携帯トイレ':
            return redirect('confirm')
        elif category == 'テキスト入力':
            return redirect('confirm')
    return render(request, 'beginner/supplie_other.html')

def supplie_medical_crutch_view(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        categories = request.session.get('categories', [])
        categories.append(category)
        request.session['categories'] = categories

        if category:
            return redirect('confirm')
    return render(request, 'beginner/supplie_medical_crutch.html')

def supplie_medical_wheelchair_view(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        categories = request.session.get('categories', [])
        categories.append(category)
        request.session['categories'] = categories
        if category:
            return redirect('confirm')
    return render(request, 'beginner/supplie_medical_wheelchair.html')

def supplie_medical_walker_view(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        categories = request.session.get('categories', [])
        categories.append(category)
        request.session['categories'] = categories
        if category:
            return redirect('confirm')
    return render(request, 'beginner/supplie_medical_walker.html')

def supplie_medical_adult_diapers_view(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        categories = request.session.get('categories', [])
        categories.append(category)
        request.session['categories'] = categories
        if category:
            return redirect('confirm')
    return render(request, 'beginner/supplie_medical_adult_diapers.html')
    
def supplie_other_clothes_view(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        categories = request.session.get('categories', [])
        categories.append(category)
        request.session['categories'] = categories

        if category == '上着':
            return redirect('supplie_other_clothes_jacket')
        elif category == 'ズボン':
            return redirect('supplie_other_clothes_pants')
    return render(request, 'beginner/supplie_other_clothes.html')

def supplie_other_shoes_view(request):
    if request.method == 'POST':
        category1 = request.POST.get('category1')
        categories = request.session.get('categories', [])
        categories.append(category1)
        category2 = request.POST.get('category2')
        categories = request.session.get('categories', [])
        categories.append(category2)
        request.session['categories'] = categories

        if category1 and category2:
            return redirect('confirm')

    return render(request, 'beginner/supplie_other_shoes.html')
def supplie_other_clothes_jacket_view(request):
    if request.method == 'POST':
        category1 = request.POST.get('category1')
        categories = request.session.get('categories', [])
        categories.append(category1)
        category2 = request.POST.get('category2')
        categories = request.session.get('categories', [])
        categories.append(category2)
        request.session['categories'] = categories

        if category1 and category2:
            return redirect('confirm')
    return render(request, 'beginner/supplie_other_clothes_jacket.html')

def supplie_other_clothes_pants_view(request):
    if request.method == 'POST':
        category1 = request.POST.get('category1')
        categories = request.session.get('categories', [])
        categories.append(category1)
        category2 = request.POST.get('category2')
        categories = request.session.get('categories', [])
        categories.append(category2)
        request.session['categories'] = categories

        if category1 and category2:
            return redirect('confirm')
            
    return render(request, 'beginner/supplie_other_clothes_pants.html')

def confirm_view(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        categories = request.session.get('categories', [])
        categories.append(category)
        request.session['categories'] = categories

        username = request.session.get('username')
        gender = request.session.get('gender')
        birthdate = request.session.get('birthdate')
        shelter_id = request.session.get('shelter_id')
        item_name = ' '.join(categories)
        quantity = request.POST.get('quantity')
        
        
        
        if username and gender and birthdate and shelter_id and item_name and quantity:
            shelter = Shelter.objects.get(pk=shelter_id)
            request_obj = beginner_account_and_item.objects.create(username=username, gender=gender, birthdate=birthdate, shelter=shelter,item_name=item_name,quantity=quantity)
            del request.session['username']
            del request.session['gender']
            del request.session['birthdate']
            del request.session['shelter_id']
            return redirect('success')
            
    return render(request, 'beginner/confirm.html')
   