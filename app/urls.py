from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trading/', views.trading, name='trading'),
    path('create/', views.create, name='trading'),
    path('login/', views.login_view, name='trading'),
    path('account/', views.account, name='account'),
]
