from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserEditForm
from .models import Avatar

# Create your views here.
def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return redirect('user_info')

            else:
                return render(request, 'accounts/login.html', {'form':form, "msj":"Datos incorrectos"})
            
        else:
            return render(request, 'accounts/login.html', {'form':form, "msj":"Credenciales incorrectas, intente nuevamente"})

    form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form':form, 'msj': ''})

def register(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render (request, 'core/padre.html', {'msj': "Usuario creado correctamente. Puede loguearse desde el navegador y editar su perfil para agregar un Avatar"})
        
    else:
        form = UserRegisterForm()
    
    return render(request, 'accounts/registro.html', {"form":form})

@login_required
def editarPerfil(request):
    user_extension_logued, _ = Avatar.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES)

        if form.is_valid():
            request.user.email = form.cleaned_data['email']
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            user_extension_logued.avatar = form.cleaned_data['avatar']
            user_extension_logued.link = form.cleaned_data['link']
            user_extension_logued.additional_description = form.cleaned_data['additional_description']

            if form.cleaned_data['password1'] != '' and form.cleaned_data['password1'] == form.cleaned_data['password2']:
                request.user.set_password(form.cleaned_data['password1'])
            
            request.user.save()
            user_extension_logued.save()

            return render(request, 'core/padre.html', {'msj': 'Usuario actualizado correctamente'})
        
        else:
            return render(request, 'accounts/editarperfil.html', {'form': form, 'msj': 'El formulario no es valido.'})
    
    form = UserEditForm(
        initial={
            'email' : request.user.email,
            'password1': '',
            'password2': '',
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'avatar': user_extension_logued.avatar,
            'link': user_extension_logued.link,
            'additional_description': user_extension_logued.additional_description,
        }
    )

    return render(request, 'accounts/editarperfil.html', {'form': form})

@login_required
def user_info(request):
    user_data, _ = Avatar.objects.get_or_create(user=request.user)
    return render(request, 'accounts/info_perfil.html', {'user_data':user_data})