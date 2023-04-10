from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

#app_name = 'renx'  urls.pyに書くものであって、views.pyに書くものでは無い。

# Create your views here.

# def top(requst):
#     return HttpResponse(b"Hello, world!!!!!!!!!!!")


## 関数ベースで書いた場合
def top(request):
    return render(request, "renx/top.html")


## クラスベースで書いた場合
class TopView(View):
    #template_name = 'renx/top.html'
    def get(self, request, *args, **kwargs):
        #return render(request, template_name)
        return render(request, "renx/top.html")

## クラスベースで書いた場合
class Mosyako1View(View):
    #template_name = 'renx/top.html'
    def get(self, request, *args, **kwargs):
        #return render(request, template_name)
        return render(request, "renx/mosyako1.html")
