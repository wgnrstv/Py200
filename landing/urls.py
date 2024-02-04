from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import path

from app.views import index_view, template_view, login_view, register_view, logout_view, user_detail_view, get_text_json

urlpatterns = [
    path('', index_view, name='index'),
    path('template/', template_view, name='template'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout', logout_view, name='logout'),
    path('profile/', user_detail_view, name='user_profile'),
    path('get/text/', get_text_json),
]
