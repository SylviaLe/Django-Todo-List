from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields import BooleanField
from django.urls import reverse

class Categories(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default="")
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        default=""
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cate_detail', args=[str(self.id)])


class Todos(models.Model):  #order matters this time so this is defined later
    title = models.CharField(max_length=255, default="")
    priority = BooleanField(default=False)
    completed = BooleanField(default=False)
    category = models.ForeignKey(
        Categories, 
        on_delete=models.CASCADE,
        related_name='todos',
        default=''
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo_detail', args=[str(self.id)])

