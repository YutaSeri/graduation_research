from django.contrib import admin
from .models import beginner_account_and_item,biginner_account_and_Other_requests 
from phone.models import Shelter

class Support_ItemAdmin(admin.ModelAdmin):
    list_display = ['username','gender', 'age','item_name','quantity','created_at', 'arrival_date','get_shelter_name',]
    def get_shelter_name(self, obj):
        return obj.shelter.shelter_name
    get_shelter_name.short_description = '避難所名'  


class Other_RequestsAdmin(admin.ModelAdmin):
    list_display = ['requests','username','created_at','get_shelter_name',]
    def get_shelter_name(self, obj):
        return obj.shelter.shelter_name
    get_shelter_name.short_description = '避難所名'


admin.site.register(beginner_account_and_item,Support_ItemAdmin)
admin.site.register(biginner_account_and_Other_requests,Other_RequestsAdmin)


