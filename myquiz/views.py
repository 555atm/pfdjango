from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.views import View
from .models import *
from .forms import QuizForm

import random

from django.urls  import reverse
# Create your views here.
from django.contrib import messages

class MyquizTopView(View):
    template_name = 'myquiz/top.html'
    def get(self, request, *args, **kwargs):
        #return render(request, template_name)
        genres = Genre.objects.all()
        return render(request, self.template_name, {
            "genres" : genres,
        })


class MyquizQuizView(View):
    template_name = 'myquiz/quiz.html'

    def get(self, request, *args, **kwargs):
    # def get(self, request, pk, *args, **kwargs):

        ##debug
        print("--self.template_name--")
        print(self.template_name)
        print("--request.session--")
        print(request.session)
        print("--request--")
        print(request)
        print("--request.session--")
        print(request.session)

        print("--request.GET--")
        print(request.GET)
        print("--request.GET.get('quiz_shuffle_list')--")
        print(request.GET.get('quiz_shuffle_list'))

        #ユーザーが選択した問題数 (全問題数の数)を取得 
        number_of_questions = request.GET.get('number_of_questions')
        # number_of_questions = int(request.GET['number_of_questions'])
        # number_of_questions = int(request.GET.get('number_of_questions'))

        monme = int(request.GET['monme'])
        print("--number_of_questions--")
        print(number_of_questions)

        ### 1問目の場合、ランダム出題リストを作り、リスト１番目のクイズ番号を出題する
        print("--monme--")
        print(monme)

        if monme == 0:
            monme += 1
            ## 問題のQuiz.idを取得し、出題リストの配列に入れる
            quiz_dict_list = []
            # メニューが0なら、全クイズのidカラムを取得
            # if menu ==0:
            quiz_ids = Quiz.objects.all().values("id")
            for quiz_id in quiz_ids:
                quiz_dict_list.append(quiz_id) 
                print("--quiz_list--")
                print(quiz_dict_list)
            # メニューが1なら、選択されたクイズジャンルのidカラムを取得
            # if menu ==1:
            # quiz_ids = Quiz.objects.filter(field="genre").values("id")[quiz_ammount]

            # idカラムの値だけを抜き出したlistを作成
            quiz_list = [item['id'] for item in quiz_dict_list]
            print("--quiz_list--")
            print(quiz_list)

            quiz_shuffle_list = random.sample(quiz_list, len(quiz_list))
            print("--quiz_shuffle_list--")
            print(quiz_shuffle_list)

            # セッションにquiz_shuffle_listを保存
            request.session['quiz_shuffle_list'] = quiz_shuffle_list

            # リストの先頭クイズ番号を出題にする
            mondai = Quiz.objects.get(id=quiz_shuffle_list[0])
            print("--mondai--")
            print(mondai)
            # # 全問題数の数を取得
            # questions = len(quiz_list)

            #1問目をこれから解くので正解数はゼロを返す 
            correct = 0

            return render(request, self.template_name, {
                "mondai" : mondai,
                "monme" : monme,
                "correct" : correct,
                # "questions" : questions,
                "number_of_questions" : number_of_questions,
                "quiz_shuffle_list":request.session['quiz_shuffle_list'],
        })

        ###2問目以降の場合、、、、
        else:
            # return render(request, 'myquiz/quiz.html')

            # １問目以降は、先ほど出題された問題idをlistから削除
            quiz_shuffle_list = []
            quiz_shuffle_list = request.GET.get('quiz_shuffle_list')
            print("-request.GET.get('quiz_shuffle_list')-")
            print(request.GET.get('quiz_shuffle_list'))
            
            pre_list = []
            # pre_list = request.GET.get('quiz_shuffle_list')
            pre_list = request.session['quiz_shuffle_list']            
            print("--pre_list--")
            print(pre_list)
            print(type(pre_list))
            quiz_shuffle_list = pre_list[1:]
            print("--quiz_shuffle_list--")
            print(quiz_shuffle_list)

            ## 出題リスト（先ほど出題した番号は削除済み）先頭を出題する
            mondai = Quiz.objects.get(id=int(quiz_shuffle_list[0]))

            correct = request.GET.get('correct')
            monme = int(request.GET.get('monme'))
            monme +=1

            #戻り値を返す
            return render(request, self.template_name, {
                "mondai" : mondai,
                "monme" : monme,
                "correct" : correct,
                # "questions" : questions,
                "number_of_questions" : number_of_questions,
                "quiz_shuffle_list":quiz_shuffle_list,
        })


    def post(self, request, pk, *args, **kwargs):
        # pass
        return redirect("myquiz/answer.html")


class MyquizAnswerView(View):

    template_name = 'myquiz/answer.html'
    def post(self, request, *args, **kwargs):
        print("--request.session--")
        print(request.session)
        print("--request.GET--")
        print(request.POST)
        monme = request.POST['monme']
        number_of_questions = request.POST['number_of_questions']
        mondai_id = request.POST['mondai_id']
        correct = int(request.POST['correct'])
        quiz_shuffle_list =[]
        quiz_shuffle_list = request.POST['quiz_shuffle_list']
        print("--monme--")
        print(monme)
        print("--number_of_questions--")
        print(number_of_questions)
        print("--mondai_id--")
        print(mondai_id)
        # ↓ 以下２行の書き方しかないのか？？（idカラムで１件抽出して、そのanswerカラムだけが欲しいとき）【要確認】
        queryset = Quiz.objects.filter(id=mondai_id)
        answer = queryset[0].answer
        # answer = Quiz.objects.get(id=mondai_id).values('answer')
        print("--answer--")
        print(answer)

        ##回答者の選択肢の値に対し正解・不正解を返す。
        user_choice = request.POST['user_choice']
        if  answer == user_choice:
            #正解と返す
            is_correct = True
            correct += 1
        else:
            #不正解と返す
            is_correct = False

        return render(request, self.template_name, {
            "user_choice" : user_choice,
            "is_correct" : is_correct,
            "answer" : answer,
            "number_of_questions" : number_of_questions,
            "correct" : correct,
            "monme" : monme,
            "quiz_shuffle_list" : quiz_shuffle_list,
        })


class MyquizResultView(View):
    template_name = "myquiz/result.html"

    def get(self, request, *args, **kwargs):
        print("--request.GET--")
        print(request.GET)
        monme = request.GET['monme']
        number_of_questions = request.GET['number_of_questions']
        correct = request.GET['correct']
        print("--monme--")
        print(monme)
        print("--number_of_questions--")
        print(number_of_questions)       
        return render(request, self.template_name, {
            "number_of_questions" : number_of_questions,
            "monme" : monme,
            "correct" : correct,
        })



class MyquizNewView(View):
    template_name = 'myquiz/new.html'

    def get(self, request, *args, **kwargs):
        # quiz = Quiz.objects.all()
        form = QuizForm()

        #return render(request, template_name)
        return render(request, self.template_name, {
            "form": form,
        })

    # @login_required
    def post(self, request, *args, **kwargs):
        login_user = self.request.user
        print("login_user")
        print(login_user)
        print("---print(request)---")
        print(request.POST)
        form = QuizForm(request.POST)
        if form.is_valid():
            print("---form-if---")
            print(form)
            quiz = form.save(commit=False)
            quiz.save()
            messages.success(request, "データの編集を完了しました。")
            return redirect("myquiz:list")
        else:
            print("---form-else---")
            print(form)
            print("---is_valid()---")
            print(form.is_valid())
            return render(self.request, self.template_name, {
                "login_user" : login_user,
                "form" : form,
            })


class MyquizEditView(View):
    template_name = 'myquiz/edit.html'
    def get(self, request, pk, *args, **kwargs):
        login_user = self.request.user
        try:
            quiz = Quiz.objects.get(id=pk)
        except Quiz.DoesNotExist:
            messages.error(request, "Quizデータの取得に失敗しました。")
            return redirect("myquiz/top.html")

        #return render(request, template_name)
        ## フォーム送信先
        send_url = reverse('myquiz:edit', kwargs={'pk': quiz.id})
        ## フォームに値を渡す
        form = QuizForm(instance=quiz)
        return render(request, self.template_name, {
            "login_user"        : login_user,
            "quiz": quiz,
            "form": form,
            "send_url" : send_url,
        })

    def post(self, request, pk, *args, **kwargs):
        login_user = self.request.user
        quiz = Quiz.objects.get(id=pk)
        print("---print(request.POST)---")
        print(request.POST)

        # ## フォーム送信先
        send_url = reverse('myquiz:top', kwargs={'pk': quiz.id})

        ## フォームに値を渡す
        form = QuizForm(request.POST, instance=quiz)

        ## フォームに問題なければ保存
        if form.is_valid():
            quiz = form.save(commit=False)
            #ジャンルが文字列で送られてくるのでgenre_id（int型）にする
            quiz.genre_id = int(request.POST['genre'])
            quiz.save()
            messages.success(request, "データの編集を完了しました。")
            return redirect("myquiz:list")
        else:
            messages.error(request, "データの編集を失敗しました。")

            return render(request, self.template_name,{
                "login_user"        : login_user,
                "quiz": quiz,
                "form" : form,
                "send_url" : send_url,
            })



class MyquizListView(View):
    template_name = 'myquiz/list.html'
    def get(self, request, *args, **kwargs):
        quizes = Quiz.objects.all()
        #return render(request, template_name)
        return render(self.request, self.template_name, {
            # "login_user"       : login_user,
            "quizes"       : quizes,
        })


class MyquizDetailView(View):
    pass



class MyquizDeleteView(View):
    template_name = "myquiz/list.html"
    def get(self, request, pk, *args, **kwargs):
      quiz = Quiz.objects.get(id = pk)
      try:
          quiz.delete()
          messages.success(request, "データの削除を完了しました")
      except:
          messages.error(request, "データの削除に失敗しました")
          return redirect("myquiz:list")
      return redirect("myquiz:list")




