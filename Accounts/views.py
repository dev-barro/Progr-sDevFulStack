# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Si le formulaire est valide, on effectue la connexion
            login(request, form.get_user())  # Connecte l'utilisateur
            return redirect('dashboard')  # Redirige vers la page du tableau de bord
    else:
        form = AuthenticationForm()

    return render(request, 'Accounts/login.html', {'form': form})
