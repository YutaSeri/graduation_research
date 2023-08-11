from django.contrib import admin

# Register your models here.
from .models import phone_Account
admin.site.register(phone_Account)

from .models import p_support_Item
admin.site.register(p_support_Item)

from .models import Shelter
admin.site.register(Shelter)