from django import forms
from .models import Repuesto, JefeAlmacen, Recepcionista, Tecnico, Marca, Camion, Pedido, Diagnostico, Administrador
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']


class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = ['nombre', 'modelo', 'marca', 'stock', 'descripcion']

class JefeAlmacenForm(forms.ModelForm):
    class Meta:
        model = JefeAlmacen
        fields = ['nombreJefe', 'usuario', 'password']

class RecepcionistaForm(forms.ModelForm):
    class Meta:
        model = Recepcionista
        fields = ['nombreRecepcionista', 'usuario', 'password']

class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ['nombreTecnico','usuario','password']

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombreMarca']

class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ['placa', 'modelo']
class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['recepcionista', 'Camion', 'Conductor', 'descripcion', 'fecha']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['recepcionista'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['Camion'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['Conductor'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['descripcion'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['fecha'].widget.attrs.update({
            'class': 'form-control',
        })

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['JefeAlmacen', 'Tecnico', 'Marca', 'Camion', 'repuesto','estado','asunto', 'cantidad','tipo_pedido', 'administrador']
