from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Shelter(models.Model):
    shelter_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Shelter_tablet' 

    def __str__(self):
        return self.shelter_name

class tablet_account_and_item(models.Model):
    GENDER_CHOICES = [
        ("男", "男"),
        ("女", "女"),
        ("未回答", "未回答"),
    ]
   

    username = models.CharField(verbose_name='名前',max_length=255,unique=False,blank=False, null=False)
    gender = models.TextField(verbose_name='性別',choices=GENDER_CHOICES, blank=False, null=False)
    age = models.IntegerField(verbose_name='年齢',validators=[MinValueValidator(0),MaxValueValidator(100)],blank=False, null=False)
    shelter = models.ForeignKey(Shelter, verbose_name='避難所選択',on_delete=models.CASCADE,default=1)
    item_name = models.CharField(verbose_name='物資一覧',max_length=255)
    quantity = models.IntegerField(verbose_name='個数')
    created_at = models.DateTimeField(default=timezone.now)
    arrival_date = models.DateTimeField(verbose_name='到着予定日',blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tablet_account_and_item'  

class tablet_account_and_Other_requests(models.Model):
    GENDER_CHOICES = [
        ("男", "男"),
        ("女", "女"),
        ("未回答", "未回答"),
    ]
   
    username = models.CharField(verbose_name='名前',max_length=255,unique=False,blank=False, null=False)
    gender = models.TextField(verbose_name='性別',choices=GENDER_CHOICES, blank=False, null=False)
    age = models.IntegerField(verbose_name='年齢',validators=[MinValueValidator(0),MaxValueValidator(100)],blank=False, null=False)
    shelter = models.ForeignKey(Shelter, verbose_name='避難所選択',on_delete=models.CASCADE,default=1)
    requests  = models.TextField(verbose_name='その他の要望',max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = 'tablet_account_and_other_requests'