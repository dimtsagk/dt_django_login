from django.urls import path
from .views import index, SignUpView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name='index'),  
    path('signup/', SignUpView.as_view(), name='signup'),  
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]