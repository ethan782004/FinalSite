from django.urls import path
from .views import index, ItemListView, CreateItemView, PostSuccessView, search

app_name = 'testapp'

urlpatterns = [
    path('', index, name='index'),
    path('items/', ItemListView.as_view(), name='_list'),
    path('post_item/', CreateItemView.as_view(), name='post_item'),
    path('post_done/', PostSuccessView.as_view(), name='post_done'),
    path('search/', search, name='search'),
]
