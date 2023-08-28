from django import forms
from .models import tablet_account_and_Other_requests

class TabletAccountAndrequestsForm(forms.ModelForm):

    class Meta:
        model = tablet_account_and_Other_requests
        fields = ['username','gender','age','shelter','requests']
        widgets = {'requests': forms.Textarea(attrs={'rows': 5,  'cols': 40,  'name': 'requests','placeholder': '避難所での問題、その他要望がありましたらご気軽にご入力ください。'})}
   
