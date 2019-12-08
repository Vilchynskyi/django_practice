from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse


from .models import Post, Comment
from .forms import PostForm, CommentForm


class IndexView(TemplateView):
    template_name = 'core/index.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_qs = Post.objects.all().order_by('-date_of_publ')
        paginator = Paginator(post_qs, 1)
        page = self.request.GET.get('page')
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = paginator.page(paginator.num_pages)

        context['post_list'] = post_list
        return context


def post_detail(request, slug):
    ctx = {}
    post = Post.objects.get(slug=slug)
    list_comments = post.comment_set.all().order_by('-date_of_publ')
    if post:
        ctx['post'] = post
        ctx['list_comments'] = list_comments
    return render(request, 'core/post_detail.html', ctx)


class WritePostView(FormView):
    template_name = 'core/write_post.html'
    form_class = PostForm
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author_name = self.request.user
        post.save()
        # user.send_user_mail('Registration', 'Welcome!')
        return super().form_valid(form)

    def form_invalid(self, form):
        return JsonResponse(form.errors)


class AddCommentView(FormView):
    template_name = 'core/add_comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author_name = self.request.user
        # comment.post =
        print(self.request.post)
