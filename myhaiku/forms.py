from django import forms

from myhaiku.models import *


class HaikuForm(forms.ModelForm):

    kami_go = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'入力してください', 'rows':'2'}),
        # widget=forms.TextInput(attrs={'placeholder':'入力してください','class':'countDown'})
    )
    naka_shichi = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'入力してください', 'rows':'2'}),
        # widget=forms.TextInput(attrs={'placeholder':'入力してください','class':'countDown'})
    )
    shimo_go = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'入力してください', 'rows':'2'}),
        # widget=forms.TextInput(attrs={'placeholder':'入力してください','class':'countDown'})
    )


    class Meta:
        model = Haiku
        fields = ('kami_go', 'naka_shichi', 'shimo_go')
        # fields = ('title', 'genre', 'tag')


