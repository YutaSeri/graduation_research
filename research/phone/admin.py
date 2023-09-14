from django.contrib import admin
from .models import Account
from .models import p_support_Item
from .models import Other_requests
from .models import Shelter

admin.site.register(Account)
admin.site.register(p_support_Item)
admin.site.register(Other_requests)
admin.site.register(Shelter)