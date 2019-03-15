from django.urls import path, re_path
from. import views
from django.contrib.auth.views import ( login,logout,password_reset,password_reset_done,
password_reset_confirm,password_reset_complete
)

app_name = 'accounts'

urlpatterns = [
    path('signUp/', views.signup_view, name='signUp'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('reset-password/',password_reset,name='reset_password'),
    #path('password_reset_email',auth_views.password_reset_email,name='email'),
    path('reset-password/done/',password_reset_done,name='password_reset_done'),
    re_path('reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})',password_reset_confirm,name='password_reset_confirm'),
    path('reset-password/complete',password_reset_complete,name='password_reset_complete'),
]
