from django import forms
from .models import biginner_account_and_Other_requests

class SearchForm(forms.Form):

    username = forms.CharField(initial='',label='名前検索',required = False)