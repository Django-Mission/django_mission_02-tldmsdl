from secrets import choice
from unicodedata import category
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Faq(models.Model):
    CATERGORY_CHOICES =[
        ('일반','일반'),
        ('계정','계정'),
        ('기타','기타'),
    ]
    question = models.TextField(verbose_name='질문')
    category = models.CharField(max_length=2, choices = CATERGORY_CHOICES)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)