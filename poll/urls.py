from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('create/', views.question_create, name='question_create'),
    path('question/<int:pk>/delete/',views.question_delete, name='question_delete'),

    path('choice/create',views.choice_create, name= 'choice_create'),
    path('choice/<int:pk>/update/',views.choice_update, name='choice_update'),
    path('choice/<int:pk>/delete/',views.choice_delete, name= 'choice_delete'),
]