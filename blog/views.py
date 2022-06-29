from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def news(request):
    posts = Post.objects.filter(is_active=True).order_by('-created_date')
    return render(request, 'posts_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
