from django.urls import path, include
from . import views
app_name = "log_in_app"
urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('log_out/', views.log_out, name = 'log_out')
    #path('user_page/', include('user_page.urls'), name = 'user_page')
]