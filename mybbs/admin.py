from django.contrib import admin
from mybbs.models import *
from myquiz.models import *
from myhaiku.models import *

#AbstractUserを継承することによって、デフォルトUserに要素を追加することができる
from django.contrib.auth.admin import UserAdmin
from .models import User



# Register your models here.



#mybbsのクラスを表示
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)

#myquizのクラスを表示
admin.site.register(Genre)
admin.site.register(Quiz)

#myhaikuのクラスを表示
admin.site.register(Haiku)


# #AbstractUserを継承することによって、デフォルトUserに要素を追加することができる
# admin.site.register(User, UserAdmin)


