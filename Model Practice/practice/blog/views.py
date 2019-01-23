from django.shortcuts import render
from .models import Blog

def home(request):
    blogs = Blog.objects    # 블로그 객체를 블로그 변수로 받음
                            # 쿼리셋 : 객체들의 목록을 전달 받음
    return render(request, 'home.html', {'blogs' : blogs})

# Create your views here.
