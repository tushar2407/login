from django.urls import path
from . import views
from django.conf.urls import url
#from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views
from django.urls import reverse
#from main.views import Home
urlpatterns=[
    #path('/',views.Signup.as_view(),name='signup'),
    #url(r'^login/$',login,{'template_name':'accounts.login.html'}),
    url(r'^$',views.home,name="home"),
    #url(r'^home/$',Home.as_view(), name="class_home")
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',LoginView.as_view(template_name='accounts/login.html'),name='login'),
    url(r'^logout/$',LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
    url(r'^account/$',views.home),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^profile/edit/$',views.edit_profile,name='edit_profile'),
    url(r'^change_password/$',views.change_password,name='change_password'),

    url(r'^reset_password/$',PasswordResetView.as_view(template_name='accounts/reset_password.html'),name='reset_password'),
    #url(r'^reset_password/$',auth_views.password_reset,name='reset_password'),   # always some error
    #url(r'^reset_password/$',PasswordResetView.as_view(template_name='accounts/reset_password.html',post_reset_redirect='main:password_reset_done',
    # email_template_name=" <something>.html"),name='reset_password'),
    url(r'^upload_file/$',views.upload_file,name="upload_file"),

    url(r'^reset_password/done/$',PasswordResetDoneView.as_view(template_name='accounts/reset_password_done.html'),name='password_reset_done'),
    url(r'^reset_password/complete/$',PasswordResetCompleteView.as_view(template_name='accounts/reset_password_done.html'),name='password_reset_complete'),
    url(r'^reset_password/confirm/$',PasswordResetConfirmView.as_view(template_name='accounts/reset_password_done.html'),name='password_reset_confirm'),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>,+)/$',PasswordResetConfirmView.as_view(template_name='accounts/reset_password_done.html'),name='password_reset_confirm'),
]