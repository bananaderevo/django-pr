from django.urls import path

from .views import SignUpView, PostCreateView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('create/', PostCreateView.as_view(), name='create'),

]