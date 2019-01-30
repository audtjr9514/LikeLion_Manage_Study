from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200) # 최대 200개의 문자로 되어있는 데이터
    pub_date = models.DateTimeField('date published') # 날짜와 시간으로 되어있는 데이터
    body = models.TextField() # 캐릭터형보다 긴 데이터

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

