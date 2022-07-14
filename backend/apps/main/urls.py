from django.urls import path

from apps.main import views

urlpatterns = [
    path('random/float/', views.random_float, name='random_float'),
    path('user/', views.user_list, name='user'),
    path('user/<int:pk>/', views.user_detail, name='user')
]
