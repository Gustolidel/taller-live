from django.urls import path
from .views import list_repuesto, create_repuesto, update_repuesto, delete_repuesto, list_Jefe, \
    create_Jefe, update_Jefe, delete_Jefe, create_Recepcionista, update_Recepcionista, delete_Recepcionista, list_Documento, \
    create_Diagnostico, update_Diagnostico, delete_Diagnostico, create_Pedido, update_Pedido, delete_Pedido
urlpatterns = [
    path('repuesto', list_repuesto, name='list_repuesto'),
    path('newRepuesto', create_repuesto, name='create_repuesto'),
    path('updateRepuesto/<int:id>/', update_repuesto, name='update_repuesto'),
    path('deleteRepuesto/<int:id>/', delete_repuesto, name='delete_repuesto'),
    path('Jefe', list_Jefe, name='list_Jefe'),
    path('newJefe', create_Jefe, name='create_Jefe'),
    path('updateJefe/<int:id>/', update_Jefe, name='update_Jefe'),
    path('deleteJefe/<int:id>/', delete_Jefe, name='delete_Jefe'),
    path('newRecepcionista', create_Recepcionista, name='create_Recepcionista'),
    path('updateRecepcionista/<int:id>/', update_Recepcionista, name='update_Recepcionista'),
    path('deleteRecepcionista/<int:id>/', delete_Recepcionista, name='delete_Recepcionista'),
    path('Documentos/', list_Documento, name='list_Documento'),
    path('newDiagnostico', create_Diagnostico, name='create_Diagnostico'),
    path('updateDiagnostico/<int:id>/', update_Diagnostico, name='update_Diagnostico'),
    path('deleteDiagnostico/<int:id>/', delete_Diagnostico, name='delete_Diagnostico'),
    path('newPedido', create_Pedido, name='create_Pedido'),
    path('updatePedido/<int:id>/', update_Pedido, name='update_Pedido'),
    path('deletePedido/<int:id>/', delete_Pedido, name='delete_Pedido'),

]
