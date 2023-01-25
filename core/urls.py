from django.urls import path 
from .views import home, somos, galeria, api, reloj, modificar, mostrar, eliminar, crear, modificar1, mostrar1, eliminar1, crear1

urlpatterns=[
    path('', home, name='home'),
    path('somos/', somos, name='somos'),
    path('galeria/', galeria, name='galeria'),
    path('api/', api, name='api'),
    path('reloj/', reloj, name='reloj'),

    #pasteles
    path('mostrar/', mostrar, name="mostrar"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('crear/',crear, name="crear"),
    path('modificar/<id>', modificar, name="modificar"),

    #clientes
    path('mostrar1/', mostrar1, name="mostrar1"),
    path('eliminar1/<id1>', eliminar1, name="eliminar1"),
    path('crear1/',crear1, name="crear1"),
    path('modificar1/<id1>', modificar1, name="modificar1"),

    
    
]