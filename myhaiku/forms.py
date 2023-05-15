from django import forms

from myhaiku.models import *

from django.core.exceptions import ValidationError

# 多言語対応する場合は必要
from django.utils.translation import gettext as _

class HaikuForm(forms.ModelForm):

    kami_go = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'入力してください'})
        # widget=forms.TextInput(attrs={'placeholder':'入力してください', 'rows':'2', 'class':'kami_input'}),
    )
    naka_shichi = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'入力してください'})
        # widget=forms.TextInput(attrs={'placeholder':'入力してください','class':'naka_input'})
    )
    shimo_go = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'入力してください'}),
    )

    def clean_kami_go(self):
        #上の句は6～8音で入力してください
        kami_go = self.cleaned_data['kami_go']
        if len(kami_go) < 5:
            raise ValidationError(
            # raise forms.ValidationError(
                '%(min_length)s文字以上で入力してください',
                code='invalid', params={'min_length':'3'})
        return kami_go

    def clean_naka_shichi(self):
        pass


    def clean_shimo_go(self):
        pass


    class Meta:
        model = Haiku
        fields = ('kami_go', 'naka_shichi', 'shimo_go')
        # fields = ('title', 'genre', 'tag')

    # 俳句入力欄の幅を広げるためcssクラスを割り当てる
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['kami_go'].widget.attrs = {'class': 'kami_input'}
        self.fields['naka_shichi'].widget.attrs = {'class': 'naka_input'}
        self.fields['shimo_go'].widget.attrs = {'class': 'shimo_input'}


