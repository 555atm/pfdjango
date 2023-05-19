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
    kami_random = forms.CharField(
        max_length=64,
        required=False,
    )
    naka_random = forms.CharField(
        max_length=64,
        required=False,
    )
    shimo_random = forms.CharField(
        max_length=64,
        required=False,
    )



    # 俳句入力欄の幅を広げるためcssクラスを割り当てる
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['kami_go'].widget.attrs = {'class': 'kami_input'}
        self.fields['naka_shichi'].widget.attrs = {'class': 'naka_input'}
        self.fields['shimo_go'].widget.attrs = {'class': 'shimo_input'}


    class Meta:
        #利用するモデルクラスを指定
        model = Haiku
        #利用するモデルのフィールドを指定
        # fields = ('kami_go', 'naka_shichi', 'shimo_go')

        fields = ('kami_go', 'naka_shichi', 'shimo_go', 'kami_random', 'naka_random', 'shimo_random')



    def clean_kami_go(self):
        #上の句は6～8音で入力してください
        kami_go = self.cleaned_data['kami_go']
        print('--kami_go--')
        print(kami_go)

        if 'a' in kami_go:
            print('--kami_go(raise前)--')
            print(kami_go)
            raise forms.ValidationError('aは利用できません')
        # if len(kami_go) < 5:
        #     raise ValidationError('5文字以上で入力してください')
        print('--kami_go(ruturn前)--')
        print(kami_go)
        return kami_go

        #     raise ValidationError(
        #     # raise forms.ValidationError(
        #         '%(min_length)s文字以上で入力してください',
        #         code='invalid', params={'min_length':'3'})
        # return kami_go

    # def clean(self):
    #     cleaned_data = super().clean()
    #     print('--cleaned_data--')
    #     print(cleaned_data)
    #     kami_go = cleaned_data.get("kami_go")
        # return kami_go

    #     if 'a' in kami_go:
    #         raise ValidationError('aは利用できません')

    #     if 'a' in shimo_go:
    #         raise ValidationError('aは利用できません')

    #     if len(shimo_go) < 5:
    #         raise ValidationError('x文字で入力してください')


            # raise ValidationError(
            # raise forms.ValidationError(
                # '%(min_length)s文字以上で入力してください',
                # code='invalid', params={'min_length':'3'})

            




