from django.forms import ModelForm
from .models import ItemPost

class ItemPostForm(ModelForm):
    class Meta:
        model = ItemPost
        fields = ['category', 'title', 'comment', 'image1', 'image2']