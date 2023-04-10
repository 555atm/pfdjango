from django import forms

from myquiz.models import *



## Genreモデルオブジェクトを取得して選択肢にするプルダウンを作成する
class GenreModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.genre_name


class QuizForm(forms.ModelForm):

    title = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'入力してください', 'rows':'2'}),
        # widget=forms.TextInput(attrs={'placeholder':'入力してください','class':'countDown'})
    )
    # genre = forms.CharField(
    #     required=False,
    #     widget=forms.Select(attrs={'rows': 1})
    # )
    # tag = forms.CharField(
    #     required=False,
    #     widget=forms.Textarea(attrs={'rows': 1})
    # )
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        required=True,
        empty_label='-- ジャンルを選択してください --',
    )

    question = forms.CharField(
        max_length=1000,
        required=True,
        widget=forms.Textarea(attrs={'placeholder':'入力してください','rows':'4'})
    )
    choice_a= forms.CharField(
        max_length=1000,
        required=True,
        widget=forms.Textarea(attrs={'placeholder':'入力してください','rows':'4'})
    )
    choice_b= forms.CharField(
        max_length=1000,
        required=True,
        widget=forms.Textarea(attrs={'placeholder':'入力してください','rows':'4'})
   )
    choice_c= forms.CharField(
        max_length=1000,
        required=True,
        widget=forms.Textarea(attrs={'placeholder':'入力してください','rows':'4'})
    )
    answer= forms.CharField(
    max_length=1000,
    required=True,
    widget=forms.Textarea(attrs={'placeholder':'入力してください','rows':'4'})
    )


    class Meta:
        model = Quiz
        fields = ('title', 'genre', 'question', 'choice_a', 'choice_b', 'choice_c', 'answer')
        # fields = ('title', 'genre', 'tag')


