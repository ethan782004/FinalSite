from django.urls import path
from .views import (
    index, login_home, ItemListView, CreateItemView, PostSuccessView,
    search, ItemDetailView
)
from . import views

app_name = 'testapp'

urlpatterns = [
    path('', login_home, name='login_home'),              # ログイン前トップ
    path('home/', index, name='index'),                   # ログイン後ホーム
    path('items/', ItemListView.as_view(), name='item_list'),
    path('post_item/', CreateItemView.as_view(), name='post_item'),
    path('post_done/', PostSuccessView.as_view(), name='post_done'),
    path('search/', search, name='search'),
    path('contact/', views.ContactView.as_view(), name='contact'),

    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
]
