from django.urls import path

from .views import BlogList
from .views import BlogCreate

urlpatterns = [
    path('', BlogList.as_view(), name='blogs'),
    path('create/', BlogCreate.as_view(), name='create_blog')
]
