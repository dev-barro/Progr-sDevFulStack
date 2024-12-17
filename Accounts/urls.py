from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', auth_views.PasswordChangeView.as_view(template_name='Accounts/register.html'), name='register'),
    # Vue intégrée pour l'inscription (non fournie par défaut, nécessite un formulaire)
    # Vue intégrée pour login
    path('login/', auth_views.LoginView.as_view(template_name='Accounts/login.html'), name='login'),

    # Vue intégrée pour logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    # Optionnel : page du tableau de bord après connexion
    path('dashboard/', auth_views.TemplateView.as_view(template_name='Accounts/dashboard.html'), name='dashboard'),
] 
