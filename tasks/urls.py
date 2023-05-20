from . import views
from django.urls import path


urlpatterns = [
    path('tasks/',views.Tasks, name='tasks'),
    path('signup/',views.Signup, name='signup'),
    path('home/',views.Home, name='home'),
    path('logout/', views.Signout, name='logout'),
    path('signin/',views.Signin, name='signin')

]