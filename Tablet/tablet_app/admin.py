from django.contrib import admin

# Register your models here.
from .models import Shelter
admin.site.register(Shelter)

from .models import tablet_account_and_item
admin.site.register(tablet_account_and_item)