from django.contrib import admin
from .models import Account, p_support_Item, Other_requests, Shelter

class SupportItemInline(admin.TabularInline):
    model = p_support_Item
    fields = ['item_name', 'quantity','created_at','arrival_date']
    readonly_fields = ['created_at']
    extra = 0  
class OtherRequestsInline(admin.TabularInline):
    model = Other_requests
    fields = ['requests', 'created_at']
    readonly_fields = ['created_at']
    extra = 0 

class ShelterAdmin(admin.ModelAdmin):
    list_display = ['shelter_name', 'created_at', ]  # 一覧表示で表示するフィールド

class AccountAdmin(admin.ModelAdmin):
    inlines = [SupportItemInline, OtherRequestsInline]
    list_display = ['username', 'gender', 'age','get_shelter_name']  # 一覧表示で表示するフィールド
    def get_shelter_name(self, obj):
        return obj.shelter.shelter_name
    get_shelter_name.short_description = 'evacuation_name'  

class SupportItemAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'quantity','get_account_name', 'get_account_gender','get_account_age','created_at', 'arrival_date','get_shelter_name',]
    list_filter = ['account__username','account__shelter__shelter_name', 'created_at','arrival_date']
    search_fields = ['item_name','account__username','account__shelter__shelter_name', 'arrival_date']
    

    def get_account_name(self, obj):
        return obj.account.username
    def get_account_gender(self, obj):
        return obj.account.gender
    def get_account_age(self, obj):
        return obj.account.age
    def get_shelter_name(self, obj):
        return obj.account.shelter.shelter_name
    get_account_name.short_description = 'name'
    get_account_gender.short_description = 'gender'
    get_account_age.short_description = 'age'
    get_shelter_name.short_description = 'evacuation_name'

class OtherRequestsAdmin(admin.ModelAdmin):
    list_display = ['requests','get_account_name','created_at','get_shelter_name',]
    list_filter = ['account__username','account__shelter__shelter_name','created_at']

    def get_account_name(self, obj):
        return obj.account.username
    def get_shelter_name(self, obj):
        return obj.account.shelter.shelter_name
    get_account_name.short_description = 'name'
    get_shelter_name.short_description = 'evacuation_name'

admin.site.register(Account, AccountAdmin)
admin.site.register(p_support_Item, SupportItemAdmin)
admin.site.register(Other_requests,OtherRequestsAdmin)
admin.site.register(Shelter,ShelterAdmin)

