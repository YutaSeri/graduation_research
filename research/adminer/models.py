from django.db import models
from phone.models import Account
from phone.models import Shelter


class Message(models.Model):
    message_text = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = 'message' 
    
    def __str__(self):
        return self.notice

class Message_middle(models.Model):
    message = models.ForeignKey(Message, verbose_name='投稿内容',on_delete=models.CASCADE)
    shelter = models.ForeignKey(Shelter, verbose_name='避難所選択',on_delete=models.CASCADE)

    class Meta:
        db_table = 'message_middle'

