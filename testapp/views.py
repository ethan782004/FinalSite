# testapp/views.py
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import ItemPost
from .forms import ItemPostForm

# トップページ（index）で商品一覧を表示
def index(request):
    items = ItemPost.objects.all().order_by('-id')  # 最新順に表示
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
    keyword = request.GET.get('q')
    products = ItemPost.objects.all().order_by('-id')  # 最新順

    # モデルのフィールド名に合わせてください（ここは title フィールドの例）
    if keyword:
        products = products.filter(title__icontains=keyword)

    return render(request, 'search.html', {
        'products': products,
        'keyword': keyword,
    })

# 商品一覧ページ（ListViewで表示する場合）
class ItemListView(ListView):
    model = ItemPost
    template_name = 'testapp/item_list.html'  
    context_object_name = 'object_list'
    ordering = ['-id']  # 最新順
