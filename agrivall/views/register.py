# from django.contrib.auth.forms import UserCreationForm
# Usamos nuestro propio form de register y lo el de django para alterar campos con BS
from agrivall.forms import RegisterForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

# usamos las funciones por defecto de validar formularios
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})