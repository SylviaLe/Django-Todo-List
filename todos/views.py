from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin 
)
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView 
from django.urls import reverse_lazy 
from .models import Todos

#Home page views
class HomePageView(TemplateView):
    template_name = 'home.html'


#Todos views
class TodoListView(ListView):
    model = Todos
    template_name = 'todo_list.html'
    

class TodoDetailView(LoginRequiredMixin, DetailView): 
    model = Todos
    template_name = 'todo_detail.html'
    context_object_name = 'todos'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = context['todos'].filter(owner=self.request.user)

        return context

class TodoCompleteView(LoginRequiredMixin, DetailView): 
    model = Todos
    template_name = 'todo_complete.html'
    context_object_name = 'todos_complete'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos_complete'] = context['todos_complete'].filter(owner=self.request.user, completed=True)

        return context


class TodoEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Todos
    fields = ('title', 'priority', 'completed', 'category')
    template_name = 'todo_edit.html'
    login_url = 'login'

    def test_func(self): 
        obj = self.get_object()
        return obj.owner == self.request.user

    

class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Todos
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('todo_list')
    login_url = 'login'

    def test_func(self): 
        obj = self.get_object()
        return obj.owner == self.request.user


class TodoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Todos
    template_name = 'todo_new.html'
    fields = ('title', 'priority', 'completed', 'category')
    login_url = 'login' 

    def form_valid(self, form): 
        form.instance.owner = self.request.user
        return super().form_valid(form)

    

#Category views:
class CategoryListView(ListView):
    pass
    

class CategoryDetailView(LoginRequiredMixin, DetailView): 
    pass
    #The list of todos belong to a category are listed here


class CategoryEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    pass

    
class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    pass


class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    pass