from django.urls import path, include
from . import views
app_name = "account"
urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('log_out/', views.log_out, name = 'log_out'),
    #path('user_page/', include('user_page.urls'), name = 'user_page')
    path('out_member/', views.out_member, name = 'out_member'),
    path('out_membership/', views.out_membership, name = 'out_membership'),
    path('login_edit/', views.login_edit, name = 'login_edit'),
]