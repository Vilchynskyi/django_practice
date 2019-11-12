from django.urls import path
from .views import (
    index_view,
    post_detail,

)


app_name = 'core'

urlpatterns = [
    path('', index_view, name='index'),
    path('posts/<slug>/', post_detail, name='post_detail'),
]
