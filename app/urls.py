from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trading/', views.trading, name='trading'),
    path('create/', views.create, name='create'),
    path('login/', views.login_view, name='login'),
    path('account/', views.account, name='account'),
]
