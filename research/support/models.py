from django.db import models
from phone_account.models import phone_Account
from django.utils import timezone

class p_support_Item(models.Model):
    item_name = models.CharField(verbose_name='物資一覧',max_length=255)
    quantity = models.IntegerField(verbose_name='個数')
    created_at = models.DateTimeField(verbose_name='申請日',default=timezone.now)
    arrival_date = models.DateTimeField(verbose_name='到着予定日',blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_account = models.ForeignKey(phone_Account, on_delete=models.CASCADE)

    class Meta:
        db_table = 'p_support_Item' 
    
    def __str__(self):
        return self.item_name
# Create your models here.

class Other_requests(models.Model):
    requests  = models.TextField(verbose_name='その他の要望',max_length=255)
    created_at = models.DateTimeField(verbose_name='投稿日',default=timezone.now, editable=False)
    phone_account = models.ForeignKey(phone_Account, on_delete=models.CASCADE)

    class Meta:
        db_table = 'other_requests' 
    
    def __str__(self):
        return self.requests
