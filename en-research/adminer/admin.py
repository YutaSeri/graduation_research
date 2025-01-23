from django.contrib import admin
from .models import Bulletin,Bulletin_middle
from phone.models import Shelter,Account


class BulletinMiddleInline(admin.TabularInline):
    model = Bulletin_middle
    extra = 1  # 一度に表示するフォームの数

class BulletinAdmin(admin.ModelAdmin):
    inlines = [BulletinMiddleInline]  
    list_display = ['title', 'notice', 'get_shelters', 'created_at']
    def get_shelters(self, obj):
        return ", ".join([shelter.shelter.shelter_name for shelter in obj.bulletin_middle_set.all()])
    get_shelters.short_description = 'Evacuation_name'  

    def save_model(self, request, obj, form, change):
        if not obj.account_id:
            obj.account = request.user
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['account'].initial = request.user.id
        return form

 
admin.site.register(Bulletin, BulletinAdmin)

admin.site.site_title = "Individual Rationed Goods Request Management System for System Administrator"
