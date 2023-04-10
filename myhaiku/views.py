from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.views import View

from myhaiku.models import *
## view側でurls.pyの名前を仕様しurl逆引きのために使用
from django.urls import reverse
## クラスベースview以下でurlを遅延評価し逆引きするためにインポート
from django.urls import reverse_lazy

import random


####### Create your views here. #######

class MyhaikuTopView(View):
    #template_name = 'renx/top.html'
    def get(self, request, *args, **kwargs):
        #return render(request, template_name)
        return render(request, "myhaiku/top.html")


class MyhaikuGameLevelView(View):
    template_name = 'myhaiku/top.html'

    def post(self, request, *args, **kwargs):

        def getRandomHiragana():
            # pass
            hiragana = ["ぁ","あ","ぃ","い","ぅ","う","ぇ","え","ぉ","お",
                "か","が","き","ぎ","く","ぐ","け","げ","こ","ご",
                "さ","ざ","し","じ","す","ず","せ","ぜ","そ","ぞ",
                "た","だ","ち","ぢ","っ","つ","づ","て","で","と","ど",
                "な","に","ぬ","ね","の","は","ば","ぱ",
                "ひ","び","ぴ","ふ","ぶ","ぷ","へ","べ","ぺ","ほ","ぼ","ぽ",
                "ま","み","む","め","も","ゃ","や","ゅ","ゆ","ょ","よ",
                "ら","り","る","れ","ろ","わ","を"]
            random_str = random.choice(hiragana)
            return random_str

        ##ユーザーが選択したゲームレベルに応じてランダム文字を生成し、top.htmlに返す
        gamelevel = request.POST.get('gamelevel')
        #もしpostされてきたのがゲームレベル３なら、上・中・下それぞれのランダム文字を一つずつ生成して返す
        if gamelevel == 3 :
            # pass
            request.session['kami_random'] = getRandomHiragana()
            request.session['naka_random'] = getRandomHiragana()
            request.session['shimo_random'] = getRandomHiragana()

            return render(self.request, self.template_name, {
                # "login_user"       : login_user,
                "kami_random"            : request.session['kami_random'],
                "naka_random"            : request.session['naka_random'],
                "shimo_random"            : request.session['shimo_random'],
            })
          
        #もしpostされてきたのがゲームレベル３なら、上・中・下それぞれのランダム文字を一つずつ生成して返す
        if gamelevel == 1 :
            pass
            request.session['kami_random'] = None
            request.session['naka_random'] = None
            request.session['shimo_random'] = None

            return render(self.request, self.template_name, {
                # "login_user"       : login_user,
                "kami_random"            : request.session['kami_random'],
                "naka_random"            : request.session['naka_random'],
                "shimo_random"            : request.session['shimo_random'],
            })


class MyhaikuNewView(View):
    #template_name = 'renx/top.html'
    def get(self, request, *args, **kwargs):
        #return render(request, template_name)
        return render(request, "myhaiku/new.html")

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


