from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def supplies_view(request):
    return render(request, 'supplies.html')

