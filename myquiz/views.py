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
from django.db.models import Count

class MyquizTopView(View):
    template_name = 'myquiz/top.html'
    def get(self, request, *args, **kwargs):
        #return render(request, template_name)
        genres = Genre.objects.all()

        #「ジャンル名：クイズ数」の表を取得
        # (つまり、クイズが、各ジャンルごとに何問あるかという行を表にするクエリ。）
        # SELECT myquiz_genre.name, COUNT(*) as count FROM myquiz_quiz INNER JOIN myquiz_genre ON myquiz_quiz.genre_id = myquiz_genre.id GROUP BY genre_id;
        # genre_question_counts = Quiz.objects.all().select_related(Genre.name).annotate(count=Count('genre_id'))

        # result = Genre.objects.annotate(count=Count('name')).values('name', 'count')
        # result = Quiz.objects.annotate(count=Count('genre_id')).select_related('genre')
        # print("--result--")
        # print(result)


        # ▼▼▼▼惜しい

        # ▼TypeError at /myquiz/top 'int' object is not iterable　というエラー
        # genre_question_counts = Quiz.objects.select_related('genre').count()

        # ▼全行表示されてしまう（カウントが全て１）　
        # genre_question_counts = Quiz.objects.select_related('genre').annotate(count=Count('genre_id'))

        # genre_question_counts = Quiz.objects.select_related('genre').all().annotate(count=Count('genre_id'))
        # genre_question_counts = Quiz.objects.select_related('genre').filter('genre_id').annotate(count=Count('genre_id'))

        # ▼惜しい
        # genre_question_counts = Quiz.objects.values('genre').annotate(count=Count('id'))
        # count = genre_question_counts.select_related(Genre)

        # genre_question_counts = Quiz.objects.values_list('genre').annotate(count=Count('id'))
        # genre_question_counts = Quiz.objects.select_related('genre').annotate(count=Count('id'))
        # genre_question_counts = Quiz.objects.select_related(Genre).count()
        # genre_question_counts = Genre.objects.annotate(num_questions=Count('genre'))
        # print('--genre_question_counts--')
        # print(genre_question_counts)
        # for item in genre_question_counts:
            # print(item['genre'],item['count'])
            # print(item[0],item[1])
        # print('--count--')
        # print(count)


        return render(request, self.template_name, {
            "genres" : genres,
            # "genre_question_counts" : genre_question_counts,
        })


class MyquizQuizView(View):
    template_name = 'myquiz/quiz.html'

    # def post(self, request, pk, *args, **kwargs):
    def post(self, request, *args, **kwargs):
        # pass

        ## １問目の場合
        # request.session['monme'] = int(request.GET.get('monme'))
        if 'start' in request.POST:
        # if 'start' in request.POST['start']:
        # if request.POST['start'] == 'start':

            #すべてのセッションを削除
            # del request.session['monme']
            # del request.session['menu']
            # del request.session['monme']
            # del request.session['number_of_questions']
            # del request.session['genre']
            # del request.session['questions']
            # del request.session['quiz_shuffle_list']
            # 間違っても、セッション全て削除しないように！！
            # request.session.clear()

            #クイズに使うセッションを全て初期化
            request.session['monme'] = 1
            print("--request.session['monme']--")
            print(request.session['monme'])
            print(type(request.session['monme']))

            ## セッションを念のため初期化
            #メニュー番号、問題数、ジャンルはクイズ終わるまで不変）
            request.session['menu'] = 0
            request.session['number_of_questions'] = 0
            request.session['genre'] = ""
            #出題リスト、正解数はクイズ中に変動
            # request.session['questions'] = 0
            request.session['quiz_shuffle_list'] =[]

            #1問目をこれから解くので正解数はゼロを返す 
            request.session['correct'] = 0
            # correct = request.session['correct']


            print("--request.session--")
            print(request.session)
            print("--request.POST--")
            print(request.POST)

            ## ユーザーが選んだメニュー番号、問題数、ジャンルをセッションの格納（クイズ終わるまで不変）
            request.session['menu'] = int(request.POST['menu'])
            # ↑参考↑　int(request.GET.get('menu'))　だとエラーになる。
            menu = request.session['menu']
            print("--menu--")
            print(type(menu))
            request.session['number_of_questions'] = int(request.POST['number_of_questions'])
            number_of_questions = request.session['number_of_questions']

            # 近日中にジャンル選択機能も追加。
            # request.session['genre'] = request.POST['genre']
            # genre = request.session['genre']


            print("--request.session--")
            print(request.session)

            ### 1問目の場合、ランダム出題リストを作り、リスト１番目のクイズ番号を出題する
            ## 問題のQuiz.idを取得し、出題リストの配列に入れる
            # 空のクイズ辞書リストを作成
            quiz_dict_list = []

            # メニューが1なら、全クイズのidカラムを取得
            if menu == 1:
                quiz_ids = Quiz.objects.all().values("id")

            # メニューが2なら、選択されたクイズジャンルのidカラムを取得
            elif menu == 2:
                selected_genre = request.POST['selected_genre']

                print("--selected_genre--")
                print(selected_genre)

                quiz_ids0 = Quiz.objects.filter(genre=selected_genre)
                print("--quiz_ids0--")
                print(quiz_ids0)


                quiz_ids = Quiz.objects.filter(genre=selected_genre).values("id")
                # quiz_ids = Quiz.objects.filter(field="genre").values("id")[quiz_ammount]
                print("--quiz_ids--")
                print(quiz_ids)

            #出題するクイズidのリストの原型（つまりdictがたくさん入ったリスト）を作成する
            for quiz_id in quiz_ids:
                quiz_dict_list.append(quiz_id) 
                print("--quiz_list--")
                print(quiz_dict_list)

            # 全クイズidだけのlistを作成
            quiz_list = [item['id'] for item in quiz_dict_list]
            print("--quiz_list--")
            print(quiz_list)

            #クイズIDリストをランダムに並び替える
            quiz_shuffle_list = random.sample(quiz_list, len(quiz_list))
            # request.session['quiz_shuffle_list'] = random.sample(quiz_list, len(quiz_list))
            print("--quiz_shuffle_list--")
            print(quiz_shuffle_list)

            # セッションにquiz_shuffle_listを保存
            request.session['quiz_shuffle_list'] = quiz_shuffle_list

            # リストの先頭クイズ番号を出題対象にする
            mondai = Quiz.objects.get(id=quiz_shuffle_list[0])
            print("--mondai--")
            print(mondai)

            return render(request, self.template_name, {
                "mondai" : mondai,
                "monme" : request.session['monme'],
                "correct" : request.session['correct'],
                "number_of_questions" : number_of_questions,
                "quiz_shuffle_list":request.session['quiz_shuffle_list'],
            })


        ###2問目以降の場合。（つまり「次の問題へ」を押した時の動作。）
        # else:
        elif 'is_next' in request.POST:
        # elif request.POST['next'] == 'next':

            # return render(request, 'myquiz/quiz.html')

            # １問目以降は、先ほど出題された問題idをlistから削除
            request.session['quiz_shuffle_list'] = request.session['quiz_shuffle_list'][1:]
            print("--request.session['quiz_shuffle_list']--")
            print(request.session['quiz_shuffle_list'])
            quiz_shuffle_list = request.session['quiz_shuffle_list']
            # quiz_shuffle_list = []
            # quiz_shuffle_list = request.POST.get('quiz_shuffle_list')
            # print("-request.POST.get('quiz_shuffle_list')-")
            # print(request.POST.get('quiz_shuffle_list'))
            
            # pre_list = []
            # # pre_list = request.POST.get('quiz_shuffle_list')
            # pre_list = request.session['quiz_shuffle_list']            
            # print("--pre_list--")
            # print(pre_list)
            # print(type(pre_list))
            # quiz_shuffle_list = pre_list[1:]
            # print("--quiz_shuffle_list--")
            # print(quiz_shuffle_list)

            ## 出題リスト（先ほど出題した番号は削除済み）先頭を出題する
            mondai = Quiz.objects.get(id=int(quiz_shuffle_list[0]))

            correct = request.POST.get('correct')


            print("--request.session--")
            print(request.session)

            # print("--request.session['monme']--")
            # print(request.session['monme'])
            # monme = request.session['monme']
            # print("--monme--")
            # print(monme)
            # print(type(monme))
            # monme +=1

            monme = int(request.POST['monme'])
            monme += 1
            print("--monme--")
            print(monme)
            print(type(monme))

            #戻り値を返す
            return render(request, self.template_name, {
                "mondai" : mondai,
                "monme" : monme,
                "correct" : correct,
                "number_of_questions" : request.session['number_of_questions'],
                "quiz_shuffle_list":quiz_shuffle_list,
            })


class MyquizAnswerView(View):

    template_name = 'myquiz/answer.html'
    def post(self, request, *args, **kwargs):
        print("--request.session--")
        print(request.session)
        print("--request.GET--")
        print(request.POST)
        monme = int(request.POST['monme'])
        number_of_questions = request.session['number_of_questions']
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

        print("--monte--")
        print(type(monme))
        print("--number_of_questions--")
        print(type(number_of_questions))


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
        # send_url = reverse('myquiz:top', kwargs={'pk': quiz.id})

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
                # "send_url" : send_url,
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




