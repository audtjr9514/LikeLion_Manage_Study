from django.db import models

# Create your models here.

class Blog(modles.Model):
    title =models.charFireld(max_length=200) 
    pub_date - models.DateTimefield('date published')
    body = models.TextField()

    #