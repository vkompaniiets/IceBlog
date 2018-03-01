from django.urls import path
from django.views.generic import RedirectView
from account import views

urlpatterns = [
    path('', RedirectView.as_view(url='/blog/login/')),
    path('login/', views.account_login, name='login'),
    path('logout/', views.account_logout, name='logout'),
    path('users/', views.show_all_users, name='all_users'),
    path('users/<int:user_id>/', views.detail, name='detail'),
]
