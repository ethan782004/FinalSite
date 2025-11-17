from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('accounts:signup_success')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # サインアップ後自動ログイン
        return response

class SignUpSuccessView(TemplateView):
    template_name = "accounts/signup_success.html"
