from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import CustomUserRegistrationForm
User = get_user_model()

def login(request):
    return render(request, 'registration/login.html') 

def logout(request):
    return render(request, 'registration/logout.html')

def registro(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'registration/registro.html', {'form': form})

def profile(request):
    return render(request, 'registration/profile.html', {'user': request.user})

def editar(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserRegistrationForm(instance=request.user)
    return render(request, 'registration/editar.html', {'form': form})