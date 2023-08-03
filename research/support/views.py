from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import p_support_Item
# Create your views here.

@login_required
def supplies_view(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')  
        quantity = request.POST.get('quantity')      
        phone_account = request.user.phone_account

        # p_support_Itemテーブルにデータを保存
        p_support_Item.objects.create(item_name=item_name,quantity=quantity,arrival_date=arrival_date,phone_account=phone_account,)
    return render(request, 'supplies.html')

    

