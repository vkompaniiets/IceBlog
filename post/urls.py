from django.urls import path

from post import views

urlpatterns = [
    path('<int:post_id>/', views.show_by_id, name='show_by_id'),
    path('<int:post_id>/update/', views.update_by_id, name='update_by_id'),
    path('create/', views.create, name='create'),
]
