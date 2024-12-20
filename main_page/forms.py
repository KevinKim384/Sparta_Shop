from django import forms
from .models import main_page, comment

class ProductForms(forms.ModelForm):
    class Meta:
        model = main_page  # 연결할 모델
        fields = ['title', 'content', 'image']  # 사용할 필드
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }
# class ProductForms(forms.Form):
#     title = forms.CharField(max_length=50)
#     content = forms.CharField(widget= forms.Textarea(attrs = {'rows': 5, 'cols' : 40}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment  # 연결할 모델
        fields = '__all__'  # 사용할 필드
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 80}),
        }
        exclude = ('article',)