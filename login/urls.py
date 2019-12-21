
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from login.views import login_redirect
from . import views
"""
adding below imports for static  files

"""
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('main.urls')),
    #path('accounts/',include('main.urls',namespace='main')),
    url(r'^$',views.login_redirect,name='login_redirect'),
]
"""
NAMESPACE :-
always assign it the value of the app you want to use in 
Plus point is when you assign different urls the same name in different apps and then you can easily direct to the  particular
app url using reverse as :---- path=revers('main:logout').lstrip('/')


"""