from django.forms import ModelForm
from .models import ItemPost

class ItemPostForm(ModelForm):
    class Meta:
        model = ItemPost
        fields = ['category', 'title', 'comment', 'image1', 'image2']

from django import forms
 
class ContactForm(forms.Form):
    name = forms.CharField(label='お名前')
    email = forms.EmailField(label='メール')
    title = forms.CharField(label='件名')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # nameフィールドのplaceholderにメッセージを登録
        self.fields['name'].widget.attrs['placeholder'] = \
          'お名前を入力してください'
        # nameフィールドを出力する<input>タグのclass属性を設定
        self.fields['name'].widget.attrs['class'] = 'form-control'
       
        # emailフィールドのplaceholderにメッセージを登録
        self.fields['email'].widget.attrs['placeholder'] = \
          'メールアドレスを入力してください'
        # emailフィールドを出力する<input>タグのclass属性を設定
        self.fields['email'].widget.attrs['class'] = 'form-control'
       
        # titleフィールドのplaceholderにメッセージを登録
        self.fields['title'].widget.attrs['placeholder'] = \
          'タイトルを入力してください'
        # titleフィールドを出力する<input>タグのclass属性を設定
        self.fields['title'].widget.attrs['class'] = 'form-control'
       
        # messageフィールドのplaceholderにメッセージを登録
        self.fields['message'].widget.attrs['placeholder'] = \
          'メッセージを入力してください'
        # messageフィールドを出力する<input>タグのclass属性を設定
        self.fields['message'].widget.attrs['class'] = 'form-control'
 