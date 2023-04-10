from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

## topページから各アプリへのリンク用。ROOT_URLCONF = 'config.urls'にしてあるので、一番最初にconfig配下のurlsやviewを参照して動く。
app_name = 'accounts'


urlpatterns = [

    path('login/', LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='accounts/login.html'
    ), name='login'),

    # path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('signup/', CreateView.as_view(
        template_name='accounts/signup.html',
        form_class=UserCreationForm,
        success_url='/',
    ), name='signup'),
]
