from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('todos/', TodoListView.as_view(), name="todo_list"),
    path('todos/complete', TodoCompleteView.as_view(), name="todo_complete"),
    path('todo/<int:pk>', TodoDetailView.as_view(), name='todo_detail'),
    path('todo/<int:pk>/edit', TodoEditView.as_view(), name='todo_edit'),
    path('todo/<int:pk>/delete', TodoDeleteView.as_view(), name='todo_complete'),
    #path('todo/new', TodoCreateView.as_view(), name='todo_new'),

    path('categories/', CategoryListView.as_view(), name="cate_list"),
    path('categories/<int:pk>', CategoryDetailView.as_view(), name="cate_detail"),
    path('categories/<int:pk>/edit', CategoryEditView.as_view(), name="cate_edit"),
    path('categories/<int:pk>/delete', CategoryDeleteView.as_view(), name="cate_delete"),
    #path('todo/new', CategoryCreateView.as_view(), name='todo_new'),
]
