# from django.urls import path,include

from renx import views
from django.urls import path
#from renx.views import top
from myhaiku import views

from config import settings
from django.urls import include
import debug_toolbar 
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

app_name = 'myhaiku'

# 追加  '__debug__/'は他のURLに影響を及ぼさないならなんでも良い

urlpatterns = [
    path('top', views.MyhaikuTopView.as_view(), name="top"),
    path('gamelevel', views.MyhaikuGameLevelView.as_view(), name="gamelevel"),
    path('new', views.MyhaikuNewView.as_view(), name="new"),
    path('confirm', views.MyhaikuConfirmView.as_view(), name="confirm"),
    path('list', views.MyhaikuListView.as_view(), name="list"),
    path('detail', views.MyhaikuDetailView.as_view(), name="detail"),
    # path('edit', views.MyhaikuEditView.as_view(), name="edit"),

    #path('', views.top),
    #path('', top, name='index'),
    #path('templates/', views.top),
]

# if settings.DEBUG:
#     urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
