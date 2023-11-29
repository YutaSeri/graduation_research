from django.db import models
from django.contrib.auth.models import AbstractBaseUser,UserManager,PermissionsMixin
from django.core.validators import EmailValidator,MinValueValidator, MaxValueValidator
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _




class Shelter(models.Model):
    shelter_name = models.CharField(verbose_name='避難所名',max_length=30)
    created_at = models.DateTimeField(verbose_name='登録日時',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時',auto_now=True)

    class Meta:
        db_table = 'Shelter' 
        verbose_name_plural = _("避難所登録")

    def __str__(self):
        return self.shelter_name


class Account(AbstractBaseUser,PermissionsMixin):
    GENDER_CHOICES = [
        ("男", "男"),
        ("女", "女"),
        ("未回答", "未回答"),
    ]
    email_validator = EmailValidator()

    username = models.CharField(verbose_name='名前',max_length=255,unique=False,blank=False, null=False)
    gender = models.CharField(verbose_name='性別',max_length=128,choices=GENDER_CHOICES, blank=False, null=False)
    age = models.IntegerField(verbose_name='年齢',validators=[MinValueValidator(0),MaxValueValidator(100)],blank=False, null=False)
    email = models.EmailField(verbose_name='メールアドレス', unique=True,blank=False, validators=[email_validator])
    password = models.CharField(verbose_name='パスワード',max_length=128,unique=True,blank=False, null=False)
    shelter = models.ForeignKey(Shelter, verbose_name='避難所選択',on_delete=models.CASCADE,default=1)
    created_at = models.DateTimeField(verbose_name='登録日時',default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='更新日時',auto_now=True)
    is_staff = models.BooleanField(default=False,help_text=_("Designates whether the user can log into this admin site."),)
    is_superuser = models.BooleanField(default=False,help_text=_("Designates that this user has all permissions without ""explicitly assigning them."),)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username','gender','age']

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        #abstract = True
        db_table = 'account'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
    
    def get_full_name(self):
     return self.username.strip()




    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

class p_support_Item(models.Model):
    item_name = models.CharField(verbose_name='物資一覧',max_length=255)
    quantity = models.IntegerField(verbose_name='個数')
    created_at = models.DateTimeField(verbose_name='申請日',default=timezone.now, editable=False)
    arrival_date = models.DateTimeField(verbose_name='到着予定日',blank=True,null=True)
    updated_at = models.DateTimeField(verbose_name='更新日時',auto_now=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE,related_name='support_items')

    class Meta:
        db_table = 'p_support_Item'
        verbose_name = "[支援物資]"
        verbose_name_plural = _("支援物資要請一覧")
    
    def __str__(self):
        return self.item_name

class Other_requests(models.Model):
    requests  = models.TextField(verbose_name='その他の要望',max_length=255,blank=False, null=False)
    created_at = models.DateTimeField(verbose_name='投稿日',default=timezone.now, editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = 'other_requests'
        verbose_name = "[その他の要望]"
        verbose_name_plural = _("その他の要望一覧")
         
   
    def __str__(self):
        return self.requests