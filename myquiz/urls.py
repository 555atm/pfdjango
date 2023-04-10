# from django.urls import path,include

from renx import views
from django.urls import path
#from renx.views import top
from myquiz import views

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

app_name = 'myquiz'


urlpatterns = [
    path('top', views.MyquizTopView.as_view(), name="top"),
    path('quiz', views.MyquizQuizView.as_view(), name="quiz"),
    path('answer', views.MyquizAnswerView.as_view(), name="answer"),
    path('result', views.MyquizResultView.as_view(), name="result"),
    # path('quiz_genre', views.MyquizTopView.as_view(), name="quiz_genre"),
    path('list', views.MyquizListView.as_view(), name="list"),
    path('new', views.MyquizNewView.as_view(), name="new"),
    path('detail', views.MyquizDetailView.as_view(), name="detail"),
    path('edit/<pk>', views.MyquizEditView.as_view(), name="edit"),
    path('delete/<pk>', views.MyquizDeleteView.as_view(), name="delete"),

    #path('', views.top),
    #path('', top, name='index'),
    #path('templates/', views.top),
]
