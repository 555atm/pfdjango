from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.views import View

from myhaiku.models import *
from myhaiku.forms import *
## view側でurls.pyの名前を仕様しurl逆引きのために使用
from django.urls import reverse
## クラスベースview以下でurlを遅延評価し逆引きするためにインポート
from django.urls import reverse_lazy

import random
from myhaiku.func import * 


####### Create your views here. #######

class MyhaikuTopView(View):
    def get(self, request, *args, **kwargs):

        # #俳句用セッションを削除-没１
        # if request.session['kami_random'] != None:
        #     del request.session['kami_random']
        # if request.session['naka_random'] != None:
        #     del request.session['naka_random']
        # if request.session['shimo_random'] != None:
        #     del request.session['shimo_random']

        # #俳句用セッションを削除-没２
        # if request.session['kami_go'] != None:
        #     del request.session['kami_go']
        # if request.session['naka_shichi'] != None:
        #     del request.session['naka_shichi']
        # if request.session['shimo_go'] != None:
        #     del request.session['shimo_go']

        # #俳句用セッションを削除
        request.session['kami_random'] = None
        request.session['naka_random'] = None
        request.session['shimo_random'] = None
        request.session['kami_go'] = None
        request.session['naka_shichi'] = None
        request.session['shimo_go'] = None

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
    def get(self, request, *args, **kwargs):
        template_name = 'myhaiku/new.html'
        form = HaikuForm()
        return render(request, template_name, {
                "kami_random"  : request.session['kami_random'],
                "naka_random"  : request.session['naka_random'],
                "shimo_random" : request.session['shimo_random'],
                "form"         : form,
        })        




# # ↓　MyhaikuConfirmViewは廃止予定
# class MyhaikuConfirmView(View):
#     template_name = 'myhaiku/confirm.html'
#     def post(self, request, *args, **kwargs):

#         #投稿された句を表示

#         #修正したければ修正

#         #修正不要なら完了画面へ遷移

#         return render(request, self.template_name, {
#                 "kami_random"            : Haiku.kami_random,
#                 "naka_random"            : Haiku.naka_random,
#                 "shimo_random"            : Haiku.shimo_random,
#                 "kami_go"            : Haiku.kami_go,
#                 "naka_shichi"            : Haiku.naka_shichi,
#                 "shimo_go"            : Haiku.shimo_go,
#         })



class MyhaikuDoneView(View):

    def post(self, request, *args, **kwargs):
        # postされた内容をformでエラーないか確認
        form = HaikuForm(request.POST)
        print('--request.POST--')
        print(request.POST)
        print('--form(validation前)--')
        print(form)

        #バリデーションでエラーなければ、句もランダム文字も保存

        form.kami_random = request.session['kami_random']
        form.naka_random = request.session['naka_random']
        form.shimo_random = request.session['shimo_random']

        if form.is_valid():

            #
            # form.save(commit=False)

            # #ランダム文字をHaikuモデルとして保存
            # form.kami_random = request.session['kami_random']
            # form.naka_random = request.session['naka_random']
            # form.shimo_random = request.session['shimo_random']

            #バリデーションエラーのない俳句をモデルとして保存
            form.save()
            print('--form(save後)--')
            print(form)


            haiku = Haiku.objects.last()

            # #ランダム文字をHaikuモデルとして保存
            # haiku.kami_random = request.session['kami_random']
            # haiku.naka_random = request.session['naka_random']
            # haiku.shimo_random = request.session['shimo_random']

            # request.session['kami_go'] = Haiku.kami_go
            # request.session['naka_shichi'] = Haiku.naka_shichi
            # request.session['shimo_go'] = Haiku.shimo_go

            #俳句用セッションを初期化する
            request.session['kami_random'] = None
            request.session['naka_random'] = None
            request.session['shimo_random'] = None
            request.session['kami_go'] = None
            request.session['naka_shichi'] = None
            request.session['shimo_go'] = None

            template_name = 'myhaiku/done.html'
            return render(request, template_name, {
                "haiku" : haiku,
                "form" : form,
            })

        #エラーならpostされた句を再度newに表示
        else:
            template_name = 'myhaiku/new.html'
            # return reverse('myhaiku:new', kargs={'form':form} )
            # reverse('myhaiku:new', args=[form] )
            # reverse(template_name, args=[form] )
            # return redirect('myhaiku:new', {"form" : form}, permanent=True)
            # return redirect('myhaiku:new', {"form" : form})

            return render(request, template_name, {
                # "haiku" : haiku,
                "form" : form,
                "kami_random"   : request.session['kami_random'],
                "naka_random"   : request.session['naka_random'],
                "shimo_random"  : request.session['shimo_random'],
                # "kami_go"       : Haiku.kami_go,
                # "naka_shichi"   : Haiku.naka_shichi,
                # "shimo_go"      : Haiku.naka_go,
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


