from django.db import models
from phone.models import Account
from phone.models import Shelter


class Bulletin(models.Model):
    title = models.CharField(verbose_name='タイトル',max_length=30)
    notice = models.TextField(verbose_name='notice',max_length=300)
    created_at = models.DateTimeField(verbose_name='created_at',auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = 'bulletin' 
        verbose_name = "[お知らせ]"
        verbose_name_plural ="自治体からのお知らせ"
    
    def __str__(self):
        return self.title
        

class Bulletin_middle(models.Model):
    bulletin = models.ForeignKey(Bulletin, verbose_name='投稿内容',on_delete=models.CASCADE)
    shelter = models.ForeignKey(Shelter, verbose_name='Evacuation_name',on_delete=models.CASCADE)

    class Meta:
        db_table = 'bulletin_middle'
    
    def __str__(self):
        return f'Bulletin Middle ID: {self.pk}, Bulletin: {self.bulletin.title}, Shelter: {self.shelter.shelter_name}'

