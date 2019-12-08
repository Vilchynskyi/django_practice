from django.urls import path
from .views import (
    IndexView,
    post_detail,
    WritePostView,
    AddCommentView,
)


app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('posts/<slug>/', post_detail, name='post_detail'),
    path('write_post/', WritePostView.as_view(), name='write_post'),
    path('add_comment/', AddCommentView.as_view(), name='add_comment'),
]
