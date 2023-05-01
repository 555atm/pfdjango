from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.views import View

from myhaiku.models import *
## view側でurls.pyの名前を仕様しurl逆引きのために使用
from django.urls import reverse
## クラスベースview以下でurlを遅延評価し逆引きするためにインポート
from django.urls import reverse_lazy

import random
from myhaiku.func import * 


####### Create your views here. #######

class MyhaikuTopView(View):
    def get(self, request, *args, **kwargs):
        #return render(request, template_name)
        return render(request, "myhaiku/top.html")


class MyhaikuGameLevelView(View):
    template_name = 'myhaiku/top.html'

    def post(self, request, *args, **kwargs):

        # return HttpResponse("level xx")

        ##ユーザーが選択したゲームレベルに応じてランダム文字を生成し、top.htmlに返す
        gamelevel = request.POST.get('gamelevel')
        print('--gamelevel--')
        print(gamelevel)
        print(type(gamelevel))
        #もしpostされてきたのがゲームレベル３なら、上・中・下それぞれのランダム文字を一つずつ生成して返す
        if gamelevel == '3' :
            # return HttpResponse("level3")
            request.session['kami_random'] = getRandomHiragana()
            request.session['naka_random'] = getRandomHiragana()
            request.session['shimo_random'] = getRandomHiragana()

            return render(self.request, self.template_name, {
                # "login_user"       : login_user,
                "gamelevel"              : gamelevel,
                "kami_random"            : request.session['kami_random'],
                "naka_random"            : request.session['naka_random'],
                "shimo_random"            : request.session['shimo_random'],
            })
        
        #もしpostされてきたのがゲームレベル３なら、上・中・下それぞれのランダム文字を一つずつ生成して返す
        elif gamelevel == '1' :
            # return HttpResponse("level1")
            request.session['kami_random'] = None
            request.session['naka_random'] = None
            request.session['shimo_random'] = None

            return render(self.request, self.template_name, {
                # "login_user"       : login_user,
                "gamelevel"              : gamelevel,
                "kami_random"            : request.session['kami_random'],
                "naka_random"            : request.session['naka_random'],
                "shimo_random"            : request.session['shimo_random'],
            })

        #def getRandomHiragana(): は func.pyに記載してある。


class MyhaikuNewView(View):
    template_name = 'myhaiku/new.html'
    def post(self, request, *args, **kwargs):

        #コメント

        #コメント

        return render(request, self.template_name, {
                "kami_random"            : request.session['kami_random'],
                "naka_random"            : request.session['naka_random'],
                "shimo_random"            : request.session['shimo_random'],
        })


class MyhaikuConfirmView(View):
    template_name = 'myhaiku/confirm.html'
    def post(self, request, *args, **kwargs):

        #コメント

        #コメント

        return render(request, self.template_name, {
                "kami_random"            : request.session['kami_random'],
                "naka_random"            : request.session['naka_random'],
                "shimo_random"            : request.session['shimo_random'],
        })


class MyhaikuListView(View):
    template_name = 'myhaiku/list.html'
    def get(self, request, *args, **kwargs):
        haikus = Haiku.objects.all()
        print("--haikus--")
        print(haikus)
        return render(self.request, self.template_name, {
            # "login_user"       : login_user,
            "haikus"            : haikus
        })



class MyhaikuDetailView(View):
    template_name = 'myhaiku/detail.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


