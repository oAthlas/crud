from django.shortcuts import render, redirect, get_object_or_404
from .models import usuario
from django.http import HttpResponse

def create_user(request):
    if request.method =='GET':
        usuariosdb = usuario.objects.all()
        return render(request, 'create_user.html' , {'usuarios': usuariosdb})
    
    elif request.method == 'POST':
        name = request.POST.get('nome')
        email = request.POST.get('email')

        user = usuario(
            name=name,
            email=email
        )

        user.save()

        return redirect('create_user')
    
def delete_user(request, id):
    ususário = get_object_or_404(usuario, id=id)
    ususário.delete()
    return redirect('create_user')

def update_user(request, id):
    ususário = get_object_or_404(usuario, id=id)

    name = request.POST.get('nome')
    email = request.POST.get('email')
    
    ususário.name = name
    ususário.email = email
    ususário.save()

    return redirect('create_user')
            