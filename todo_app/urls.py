from django.urls import path
from todo_app import views

urlpatterns = [
    path('id/', views.TodoAPIView.as_view()),
    path('id/<int:pk>/', views.TodoAPIView.as_view(),)
]