from django.db import models
from phone.models import Account
from phone.models import Shelter


class Bulletin(models.Model):
    notice = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = 'bulletin' 
    
    def __str__(self):
        return self.notice

class Bulletin_middle(models.Model):
    bulletin = models.ForeignKey(Bulletin, verbose_name='投稿内容',on_delete=models.CASCADE)
    shelter = models.ForeignKey(Shelter, verbose_name='避難所選択',on_delete=models.CASCADE)

    class Meta:
        db_table = 'bulletin_middle'
    
    def __str__(self):
        return f'Bulletin Middle ID: {self.pk}, Bulletin: {self.bulletin.notice}, Shelter: {self.shelter.shelter_name}'

