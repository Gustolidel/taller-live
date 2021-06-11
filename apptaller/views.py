from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .models import Camion, Tecnico, Diagnostico, Recepcionista, Pedido, Repuesto, JefeAlmacen, Marca, Administrador
from .forms import RepuestoForm, JefeAlmacenForm, CreateUserForm, RecepcionistaForm, TecnicoForm, MarcaForm, CamionForm, DiagnosticoForm, PedidoForm
from django.contrib.auth.models import Group
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
# VIDEO TUTORIAL LOGIN
# https://www.youtube.com/watch?v=tUqUdu0Sjyc
# Create your views here.
@login_required(login_url='login')
@admin_only
def Principal(request):
    return render(request, 'registration/Principal.html')

def Inicio(request):
    return render(request, 'Inicio.html')

@unauthenticated_user
def RegisterPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='recepcionista')
            user.groups.add(group)
            Recepcionista.objects.create(
                user=user,
                nombreRecepcionista=username
            )
            messages.success(request, 'Cuenta registrada correctamente para ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)

@unauthenticated_user
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_Jefe')
        else:
            messages.info(request, 'Usuario o password son incorrectos')
    context = {}
    return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['recepcionista'])
def UserPage(request):
    misdiagnosticos = request.user.recepcionista.diagnostico_set.all()
    print('DIAGNOSTICOS: ', misdiagnosticos)

    pedido_aprobado_count = misdiagnosticos.filter(Conductor=1).count()
    context = {'misdiagnosticos': misdiagnosticos, 'pedido_aprobado_count': pedido_aprobado_count}
    return render(request, 'registration/User.html', context)

@login_required(login_url='login')
@admin_only
def AdminPage(request):
    context = {}
    return render(request, 'registration/Administrador.html', context)


@login_required(login_url='login')
@admin_only
def list_repuesto(request):
    repuestos = Repuesto.objects.all()
    return render(request, 'registration/Documentos.html', {'repuestos': repuestos})


@login_required(login_url='login')
@admin_only
def create_repuesto(request):
    form = RepuestoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_Jefe')
    return render(request, 'repuestos-form.html', {'form': form})

@login_required(login_url='login')
@admin_only
def update_repuesto(request, id):
    repuestos = Repuesto.objects.get(id=id)
    form = RepuestoForm(request.POST or None, instance=repuestos)
    if form.is_valid():
        form.save()
        return redirect('list_Jefe')
    return render(request, 'repuestos-form.html', {'form': form, 'repuesto': repuestos})

@login_required(login_url='login')
@admin_only
def delete_repuesto(request, id):
    repuesto = Repuesto.objects.get(id=id)
    if request.method == 'POST':
        repuesto.delete()
        return redirect('list_Jefe')
    return render(request, 'repuesto-delete-confirm.html', {'repuesto': repuesto})

@login_required(login_url='login')
@admin_only
def list_Jefe(request):
    jefes = JefeAlmacen.objects.all()
    usuarios = User.objects.all()
    recepcionistas = Recepcionista.objects.all()
    jefes_count=jefes.count()
    recepcionistas_count = recepcionistas.count()
    usuarios_count = usuarios.count()
    return render(request, 'registration/Administrador.html', {'jefes': jefes,'recepcionistas':recepcionistas,
                                                               'jefes_count': jefes_count,'recepcionistas_count':recepcionistas_count,
                                                               'usuarios_count': usuarios_count})

@login_required(login_url='login')
@admin_only
def create_Jefe(request):
    form = JefeAlmacenForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_Jefe')
    return render(request, 'jefealmacen-form.html', {'form': form})

@login_required(login_url='login')
@admin_only
def update_Jefe(request, id):
    jefes = JefeAlmacen.objects.get(id=id)
    form = JefeAlmacenForm(request.POST or None, instance=jefes)
    if form.is_valid():
        form.save()
        return redirect('list_Jefe')
    return render(request, 'jefealmacen-form.html', {'form': form, 'jefe': jefes})

@login_required(login_url='login')
@admin_only
def delete_Jefe(request, id):
    jefe = JefeAlmacen.objects.get(id=id)
    if request.method == 'POST':
        jefe.delete()
        return redirect('list_Jefe')
    return render(request, 'jefealmacen-delete-confirm.html', {'jefe': jefe})

@login_required(login_url='login')
@admin_only
def create_Recepcionista(request):
    form = RecepcionistaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_Jefe')
    return render(request, 'recepcionista-form.html', {'form': form})

@login_required(login_url='login')
@admin_only
def update_Recepcionista(request, id):
    recepcionistas = Recepcionista.objects.get(id=id)
    form = RecepcionistaForm(request.POST or None, instance=recepcionistas)
    if form.is_valid():
        form.save()
        return redirect('list_Jefe')
    return render(request, 'recepcionista-form.html', {'form': form, 'recepcionista': recepcionistas})

@login_required(login_url='login')
@admin_only
def delete_Recepcionista(request, id):
    recepcionista = Recepcionista.objects.get(id=id)
    if request.method == 'POST':
        recepcionista.delete()
        return redirect('list_Jefe')
    return render(request, 'recepcionista-delete-form.html', {'recepcionista': recepcionista})


@login_required(login_url='login')
@allowed_users(allowed_roles=['recepcionista', 'admin'])
def list_Documento(request):
    diagnostico = Diagnostico.objects.all()
    pedido = Pedido.objects.all()
    diagnostico_count = diagnostico.count()
    pedido_count = pedido.count()

    return render(request, 'registration/Documentos.html', { 'diagnosticos': diagnostico, 'pedidos': pedido,
                                                               'pedido_count': pedido_count,
                                                               'diagnosticos_count': diagnostico_count})
@login_required(login_url='login')
@admin_only
def create_Diagnostico(request):
    form = DiagnosticoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_Documento')
    return render(request, 'diagnostico-form.html', {'form': form})

@login_required(login_url='login')
@admin_only
def update_Diagnostico(request, id):
    diagnosticos = Diagnostico.objects.get(id=id)
    form = DiagnosticoForm(request.POST or None, instance=diagnosticos)
    if form.is_valid():
        form.save()
        return redirect('list_Documento')
    return render(request, 'diagnostico-form.html', {'form': form, 'diagnostico': diagnosticos})

@login_required(login_url='login')
@admin_only
def delete_Diagnostico(request, id):
    diagnostico = Diagnostico.objects.get(id=id)
    if request.method == 'POST':
        diagnostico.delete()
        return redirect('list_Documento')
    return render(request, 'diagnostico-delete-form.html', {'diagnostico': diagnostico})

@login_required(login_url='login')
@admin_only
def create_Pedido(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_Documento')
    return render(request, 'pedido-form.html', {'form': form})

@login_required(login_url='login')
@admin_only
def update_Pedido(request, id):
    pedidos = Pedido.objects.get(id=id)
    form = PedidoForm(request.POST or None, instance=pedidos)
    if form.is_valid():
        form.save()
        return redirect('list_Documento')
    return render(request, 'pedido-form.html', {'form': form, 'pedido': pedidos})

@login_required(login_url='login')
@admin_only
def delete_Pedido(request, id):
    pedido = Pedido.objects.get(id=id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('list_Documento')
    return render(request, 'pedido-delete-form.html', {'pedido': pedido})
