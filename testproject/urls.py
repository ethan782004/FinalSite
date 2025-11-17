from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # testapp のページ（トップ）
    path('', include('testapp.urls')),

    # accounts アプリ（signup, signup_success）
    path('accounts/', include('accounts.urls')),

    # Django 標準の login/logout
    path('accounts/', include('django.contrib.auth.urls')),
]
