from django.shortcuts import render, get_object_or_404
from .models import Blogpost

# Create your views here.
def blog_list(request):
    posts = Blogpost.objects.all()
    return render(request, 'blog_list.html',{'posts':posts})

def blog_detail(request, blog_id):
    post = get_object_or_404(Blogpost, id=blog_id)
    return render(request, 'blog_detail.html', {'post': post})
