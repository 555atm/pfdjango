from django.shortcuts import render
from django.views import View

## djangoのユーザーモデルのインポート
from django.contrib.auth.models import User as DjangoUser
from django.contrib.messages import constants as messages
## djangoのメッセージ機能を利用しリダイレクト後にメッセージを表示する
from django.contrib import messages
## formをすべてインポート

from ..forms import LoginForm


# # Create your views here.


class LoginView(View):
    def get(self, request, *args, **kwargs):
        # self.template_name = 'accounts/login.html'
        form = LoginForm(request.POST)

        return render(request, self.template_name)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'accounts/logout.html'
        return render(request, template_name)

