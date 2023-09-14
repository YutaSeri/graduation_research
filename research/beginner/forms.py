from django import forms
from .models import biginner_account_and_Other_requests

class BiginneraccountandOtherrequests(forms.ModelForm):

    class Meta:
        model = biginner_account_and_Other_requests
        fields = ['username','gender','age','shelter','requests']
        widgets = {'requests': forms.Textarea(attrs={'rows': 5,  'cols': 40,  'name': 'requests','placeholder': '避難所での問題、その他要望がありましたらご気軽にご入力ください。'})}

class SearchForm(forms.Form):

    username = forms.CharField(initial='',label='名前検索',required = False)