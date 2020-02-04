from django.urls import include, path
from . import views
urlpatterns = [
path('cliente/', views.cliente, name='cliente'),
path('produto/', views.produto, name='produto'),
path('pedido/', views.pedido, name='pedido'),
path('relatorio/', views.relatorio, name='relatorio'),
path('editar/<int:id_pedido>/', views.editar, name='editar'),
]