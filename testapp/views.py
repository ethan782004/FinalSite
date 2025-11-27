from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import ItemPost
from .forms import ItemPostForm
from django.views.generic import FormView
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from .models import ItemPost, Category
from django.shortcuts import render, redirect
from django.db.models import Q


# ログイン前トップページ

def login_home(request):
    """
    ログイン前に表示するホームページ
    """
    if request.user.is_authenticated:
        return redirect('testapp:index')
    return render(request, 'login_home.html')  # ログイン前用テンプレート


# ログイン後トップ（商品一覧）

def index(request):
    items = ItemPost.objects.all().order_by('-id')
    return render(request, 'index.html', {
        'object_list': items
    })


# 出品ページ

@method_decorator(login_required, name='dispatch')
class CreateItemView(CreateView):
    form_class = ItemPostForm
    template_name = "post_item.html"
    success_url = reverse_lazy('testapp:post_done')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)


# 投稿完了ページ

class PostSuccessView(TemplateView):
    template_name = 'post_success.html'


# 検索ページ

def search(request):
    keyword = request.GET.get("q", "")
    selected_category = request.GET.get("category", "")

    products = ItemPost.objects.all()

    #  キーワード検索（タイトル＋コメント）
    if keyword:
        products = products.filter(
            Q(title__icontains=keyword) |
            Q(comment__icontains=keyword)
        )

    # 🏷 カテゴリ検索
    if selected_category:
        products = products.filter(category_id=selected_category)

    categories = Category.objects.all()

    return render(request, "search.html", {
        "products": products,
        "keyword": keyword,
        "categories": categories,
        "selected_category": selected_category,
    })



# 商品一覧ページ

class ItemListView(ListView):
    model = ItemPost
    template_name = 'testapp/item_list.html'
    context_object_name = 'object_list'
    ordering = ['-id']


# 商品詳細ページ（今回追加）

class ItemDetailView(DetailView):
    model = ItemPost
    template_name = 'item_detail.html'
    context_object_name = 'item'


# お問い合わせフォーム

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('testapp:contact')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']

        subject = f'問い合わせ: {title}'
        message = (
            f"送信者名: {name}\n"
            f"メールアドレス: {email}\n"
            f"タイトル: {title}\n"
            f"メッセージ:\n{message}"
        )
        from_email = 'spr2540092@stu.o-hara.ac.jp'
        to_list = ['spr2540092@stu.o-hara.ac.jp']

        email_message = EmailMessage(subject, message, from_email, to_list)
        email_message.send()

        messages.success(self.request, '問い合わせ正常に送信されました。')
        return super().form_valid(form)
