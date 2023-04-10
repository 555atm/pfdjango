from django.shortcuts import render
from django.contrib.auth.decorators import login_required
## テンプレートの描画リダイレクトに使用
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View

from mybbs.models import *
from mybbs.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#app_name = 'renx'  urls.pyに書くものであって、views.pyに書くものでは無い。

## view側でurls.pyの名前を仕様しurl逆引きのために使用
from django.urls import reverse
## クラスベースview以下でurlを遅延評価し逆引きするためにインポート
from django.urls import reverse_lazy



##### Create your views here.

# def top(requst):
#     return HttpResponse(b"Hello, world!!!!!!!!!!!")

# ## 関数ベースで書いた場合
# def top(request):
#     return render(request, "mybbs/top.html")

## クラスベースで書いた場合
class MybbsTopView(View):
    template_name = 'mybbs/top.html'
    def get(self, request, *args, **kwargs):
        posts = Post.objects.prefetch_related("tag").all()
        # tags = Tag.objects.select_related("")
        # posts = Post.objects.all().select_related("category")

        print("--posts--")
        print(posts)
        for post in posts:
            print(post)
            print(post.category)
            print(post.tag)
        return render(self.request, self.template_name, {
            # "login_user"       : login_user,
            "posts"            : posts,
        })

class MybbsNewView(View):
    template_name = 'mybbs/new.html'
    def get(self, request, *args, **kwargs):
        post = Post.objects.all().select_related
        form = PostForm()
        #return render(request, template_name)
        return render(self.request, self.template_name, {
            # "login_user"       : login_user,
            "post"            : post,
            "form"             : form,
        })
    # @login_required
    def post(self, request, *args, **kwargs):
        print("---print(request.POST)---")
        print(request.POST)
        login_user = self.request.user
        # category = Category.objects.filter(id=self.kwargs['category'])
        form = PostForm(request.POST)
        # form = PostForm(request.POST, instance=Post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.categoryはstringで送られてくるのでintにcastする
            post.category_id = int(request.POST["category"])
            # post.category_id = self.kwargs['pk']
            # post.created_by = request.user
            post.save()
            # return render(request, "mybbs/top.html")
            return redirect("mybbs:top")
            # return redirect("mybbs:top", post_id=post_id)
        else:
            return render(self.request, self.template_name, {
                "login_user"      : login_user,
                "form"            : form,
            })


class MybbsDetailView(View):
    template_name = 'mybbs/detail.html'
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        # post = Post.objects.get(id=post_id)
        form = PostForm(instance=Post)
        print("--form--")
        print(form)
        #return render(request, template_name)
        return render(self.request, self.template_name, {
        # return render(request, self.template_name, {
            # "login_user"       : login_user,
            "post"            : post,
            "form"            : form,
        })



class MybbsEditView(View):
    #template_name = 'renx/top.html'
    def get(self, request, pk, *args, **kwargs):
        login_user = self.request.user
        # user_setting_level = check_user_custom_setting(request,login_user)
        # if not user_setting_level:
        #     messages.error(request, "権限がありません")
        #     return redirect("pasch_cms:top")

        print("--request.GET--")
        print(request.GET)

        try:
            post = Post.objects.get(id=pk)
            tags = Tag.objects.all()
            post.tag.set(tags)

        except Post.DoesNotExist:
            messages.error(request, "Postデータの取得に失敗しました。")
            return redirect("mybbs/top.html")

        ## フォーム
        form = PostForm(instance=post)


        ## 以下だと長いので没
        # form = PostForm(initial={
        #     'title': post.title,
        #     'content': post.content,
        #     })

        # ## フォームに値を渡す
        # form = PostForm(instance=PostForm)

        ## フォーム送信先
        send_url = reverse('mybbs:edit', kwargs={'pk': post.id})


        #return render(request, template_name)
        return render(request, "mybbs/edit.html", {
            "login_user"        : login_user,
            "post"              : post,
            # "user_setting_level": user_setting_level,
            "form"              : form,
            "send_url"          : send_url,
            # "page_title"        : self.page_title,
        })

    def post(self, request, pk, *args, **kwargs):
        login_user = self.request.user
        post = Post.objects.get(id=pk)
        tags = Tag.objects.all()
        post.tag.set(tags)
        ## フォーム送信先
        send_url = reverse('mybbs:edit', kwargs={'pk': post.id})
        ## フォームに値を渡す
        form = PostForm(request.POST, instance=post)
        ## フォームに問題なければ保存
        if form.is_valid():
            form.save()
            messages.success(request, "データの編集を完了しました。")
            return redirect("mybbs:top")
        else:
            return render(self.request, self.template_name, {
                "login_user"        : login_user,
                # "user_setting_level": user_setting_level,
                "form"              : form,
                "send_url"          : send_url,
                # "page_title"        : self.page_title,
                # "submit_btn_title"  : self.submit_btn_title,
            })


class MybbsDeleteView(View):
    template_name = "mybbs/top.html"
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        try:
            post.delete()
            messages.success(request, "データの削除を完了しました")
        except:
            messages.error(request, "データの削除に失敗しました")
            return redirect("mybbs:top")
        return redirect("mybbs:top")




