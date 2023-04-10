
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import views
from django.urls import path,include
#from config.views import index

#from django.contrib import admin
#from config import views
#from myapp.renx import views





## topページから各アプリへのリンク用。ROOT_URLCONF = 'config.urls'にしてあるので、一番最初にconfig配下のurlsやviewを参照して動く。
#   上記（configがベースアプリ）の場合、　右の記述　app_name = 'config'　は不要のはず。

#app_name = 'config'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),

    # 7.1.1 Djangoの提供する認証機能（２１０ページ）
    # path('accounts/', include('django.contrib.auth.urls')),

    path('', views.IndexView.as_view(), name=""),
    #path('', views.TopView.as_view(), name=""),

    #path('', top),
    #path('', include('front.urls')),
    #path('', include('urls')),
    path('renx/', include('renx.urls')),
    path('mybbs/', include('mybbs.urls')),
    path('myquiz/', include('myquiz.urls')),
    path('myhaiku/', include('myhaiku.urls')),
    #path('myhaiku/', include('myhaiku.urls')),
]
