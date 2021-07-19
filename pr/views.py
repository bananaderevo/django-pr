from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from django.urls import reverse_lazy
from django.views import generic

from .models import *


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = 'login/'
    template_name = 'registration/signup.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['text', 'comments']
    success_url = ''
    template_name = 'pr/create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.author = post.user
        post.author.id = self.request.user.id
        post.save()
        self.object = post
        return super().form_valid(form)
