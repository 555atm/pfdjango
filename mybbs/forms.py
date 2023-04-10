from django import forms

from mybbs.models import *


class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        required=True,
    )

    class Meta:
        model = Category
        fields = ('name',)

class TagForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        required=True,
    )

    class Meta:
        model = Tag
        fields = ('name',)


class PostForm(forms.ModelForm):

    title = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'入力してください'})
        # widget=forms.TextInput(attrs={'placeholder':'入力してください','class':'countDown'})
    )
    content = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 3})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label='--カテゴリーを選択してください--'
        # widget=forms.widgets.Select(attrs={'rows': 1})
    )

    tag = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 1})
    )


    class Meta:
        model = Post
        fields = ('title', 'content', 'category','tag',)
        # fields = ('title', 'content', 'category', 'tag')


