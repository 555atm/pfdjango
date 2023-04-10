from renx import views
from django.urls import path
#from renx.views import top
from mybbs import views


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


## topページから各アプリへのリンク用。ROOT_URLCONF = 'config.urls'にしてあるので、一番最初にconfig配下のurlsやviewを参照して動く。
##　↓ ↑
## renx用
app_name = 'mybbs'


urlpatterns = [
    path('top', views.MybbsTopView.as_view(), name="top"),
    path('new', views.MybbsNewView.as_view(), name="new"),
    path('<pk>/edit', views.MybbsEditView.as_view(), name="edit"),
    path('<pk>/detail', views.MybbsDetailView.as_view(), name="detail"),
    path('<pk>/delete', views.MybbsDeleteView.as_view(), name="delete"),
    # path('<int:pk>/detail', views.MybbsDetailView.as_view(), name="detail"),
    #path('', views.top),
    #path('', top, name='index'),
    #path('templates/', views.top),
]
