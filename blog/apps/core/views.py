from django.shortcuts import render
from .models import Post


def index_view(request):
    ctx = {}
    ctx['post_list'] = Post.objects.all().order_by('-date_of_publ')
    return render(request, 'core/index.html', ctx)


def post_detail(request, slug):
    ctx = {}
    post = Post.objects.get(slug=slug)
    list_comments = post.comment_set.all().order_by('-date_of_publ')
    if post:
        ctx['post'] = post
        ctx['list_comments'] = list_comments
    return render(request, 'core/post_detail.html', ctx)
