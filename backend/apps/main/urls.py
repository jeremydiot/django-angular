from django.urls import path

from apps.main import views

urlpatterns = [
    path('random/float/', views.random_float)
]
