from django.urls import path
from . import views
app_name = "log_in_app"
urlpatterns = [
    path('new_user/', views.new_user, name = 'new_user'),
    path('log_in/', views.log_in, name = 'log_in'),
]