from django.urls import path
from todo_app import views

urlpatterns = [
    path('todos/', views.TodoAPIView.as_view()),
    path('todos/<int:pk>/', views.TodoAPIView.as_view()),
]