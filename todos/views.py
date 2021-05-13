from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin 
)
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView 
from django.urls import reverse_lazy 
from .models import Todos, Categories

#Home page views
class HomePageView(TemplateView):
    template_name = 'home.html'


#Todos views
class TodoListView(ListView):
    model = Todos
    template_name = 'todo_list.html'
    context_object_name = 'todos'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = context['todos'].filter(owner=self.request.user)
        context['total'] = context['todos'].filter(owner=self.request.user).count()

        return context
    

class TodoDetailView(LoginRequiredMixin, DetailView): 
    model = Todos
    template_name = 'todo_detail.html'
    context_object_name = 'todo'
    login_url = 'login'
    

class TodoCompleteView(LoginRequiredMixin, ListView): 
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
    context_object_name = 'todo'
    login_url = 'login'

    def test_func(self): 
        obj = self.get_object()
        return obj.owner == self.request.user


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todos
    template_name = 'todo_new.html'
    fields = ('title', 'priority', 'category')
    login_url = 'login' 

    def form_valid(self, form): 
        form.instance.owner = self.request.user
        return super().form_valid(form)

    

#Category views:
class CategoryListView(ListView):
    model = Categories
    template_name = 'category_list.html'
    context_object_name = 'cates'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cates'] = context['cates'].filter(owner=self.request.user)

        return context
    

class CategoryDetailView(LoginRequiredMixin, DetailView): 
    model = Categories
    template_name = 'category_detail.html'
    context_object_name = 'cate'
    login_url = 'login'


class CategoryEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Categories
    fields = ('title', 'description')
    template_name = 'category_edit.html'
    login_url = 'login'

    def test_func(self):
        cate = self.get_object()
        return cate.owner == self.request.user

    def handle_no_permission(self):
        return redirect('cate_list')

    
class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Categories
    template_name = 'category_delete.html'
    success_url = reverse_lazy('cate_list')
    context_object_name = 'cate'
    login_url = 'login'

    def test_func(self):
        cate = self.get_object()
        return cate.owner == self.request.user

    def handle_no_permission(self):
        return redirect('cate_list')


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Categories
    template_name = 'category_new.html'
    fields = ('title', 'description' )
    login_url = 'login'

    def form_valid(self, form): 
        form.instance.owner = self.request.user
        return super().form_valid(form)