from django.shortcuts import render

def user_detail_view(request):
    
    return render(request, 'user_detail.html')

