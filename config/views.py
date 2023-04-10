from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views import View

## djangoのログイン認証をインポート
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

app_name = 'config'

## 関数ベースで書いた場合
# def index(request):
#     #render(request, "index.html")
#     TemplateResponse(request, "index.html")


## クラスベースで書いた場合
# class IndexView(View):
class IndexView(LoginRequiredMixin,View):
    # login_url = "accounts:login"
    #template_name = 'myapp/index.html'
    def get(self, request, *args, **kwargs):
        #return render(request, template_name)
        return render(request, "index.html")


