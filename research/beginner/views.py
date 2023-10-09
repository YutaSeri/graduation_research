from django.shortcuts import render, redirect
from .forms import BiginneraccountandOtherrequests
from .forms import SearchForm
from .models import beginner_account_and_item
from phone.models import Shelter

def home_view(request):
    return render(request, 'beginner/home.html')

def item_view(request):
    shelters = Shelter.objects.all()
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
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        quantity = request.POST.get('quantity', 0)
        shelter_id = request.POST.get('shelter')
        beginner_account_and_item.objects.create(username=username,gender=gender,age=age,item_name=item_name,shelter_id=shelter_id,quantity=quantity)
        return redirect('success')

    return render(request, 'beginner/supplie.html', {'shelters': shelters})

def success_view(request):
    return render(request, 'beginner/success.html')

def supplie_view(request):
    return render(request, 'beginner/supplie.html')

def requests_view(request):
    if request.method == 'POST':
        form = BiginneraccountandOtherrequests(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  
    else:
        form = BiginneraccountandOtherrequests()
    param = {
        'form': form
    }  
    return render(request, 'beginner/requests.html', param)

def other_requests_view(request):
    return render(request, 'beginner/requests.html')

def search_results_view(request):
    username = request.GET.get('q', '')
    results = beginner_account_and_item.objects.filter(username__icontains=username)
    return render(request, 'beginner/search_results.html', {'results': results, 'username': username})

def search_view(request):
    return render(request, 'beginner/search.html')
    

