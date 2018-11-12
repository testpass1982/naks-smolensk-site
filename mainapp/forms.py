from django import forms

from .models import Post, Article, Document

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'tags', 'category', 'author', 'text', 'created_date', 'published_date')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'tags', 'author', 'text', 'created_date', 'published_date')
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ('title', 'document', 'tags', 'created_date')
    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
