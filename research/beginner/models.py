from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from phone.models import Shelter


class beginner_account_and_item(models.Model):
    username = models.CharField(verbose_name='名前',max_length=255,unique=False,blank=False, null=False)
    gender = models.TextField(verbose_name='性別',blank=False, null=False)
    age = models.IntegerField(verbose_name='年齢',validators=[MinValueValidator(0),MaxValueValidator(100)],blank=False, null=False)
    shelter = models.ForeignKey(Shelter, verbose_name='避難所選択',on_delete=models.CASCADE,default=1)
    item_name = models.CharField(verbose_name='物資一覧',max_length=255)
    quantity = models.IntegerField(verbose_name='個数')
    created_at = models.DateTimeField(verbose_name='登録日時',default=timezone.now)
    arrival_date = models.DateTimeField(verbose_name='到着予定日',blank=True, null=True)
    updated_at = models.DateTimeField(verbose_name='更新日時',auto_now=True)

    class Meta:
        db_table = 'beginner_account_and_item'  

class biginner_account_and_Other_requests(models.Model):
    username = models.CharField(verbose_name='名前',max_length=255,unique=False,blank=False, null=False)
    shelter = models.ForeignKey(Shelter, verbose_name='避難所選択',on_delete=models.CASCADE,default=1)
    requests  = models.TextField(verbose_name='その他の要望',max_length=255,blank=False, null=False)
    created_at = models.DateTimeField(verbose_name='登録日時',default=timezone.now)
    class Meta:
        db_table = 'biginner_account_and_Other_requests'