from django.shortcuts import render, get_object_or_404
from .models import Blog

def home(request):
    blogs = Blog.objects    # 블로그 객체를 블로그 변수로 받음
                            # 쿼리셋 : 객체들의 목록을 전달 받음
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

# Create your views here.
