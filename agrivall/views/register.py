# from django.contrib.auth.forms import UserCreationForm
# Usamos nuestro propio form de register

from django.contrib.auth.forms import UserCreationForm
from agrivall.forms import RegistroForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

# usamos las funciones por defecto de validar formularios
def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistroForm()
    
    return render(request, 'auth/register.html', {'form': form})