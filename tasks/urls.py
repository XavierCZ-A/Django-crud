from . import views
from django.urls import path


urlpatterns = [
    path('tasks/',views.Tasks, name='tasks'),
    path('signup/',views.Signup, name='signup')
]