from django.views.generic import CreateView, TemplateView   # TemplateView を追加
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

# サインアップビュー
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('accounts:signup_success')  # サインアップ成功ページ

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # 自動ログイン
        return response

# サインアップ成功ページビュー
class SignUpSuccessView(TemplateView):
    template_name = "accounts/signup_success.html"