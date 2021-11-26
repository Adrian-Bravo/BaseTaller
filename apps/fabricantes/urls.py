from django.urls import path, include
from apps.fabricantes.views import index,fabricanteCreate,fabricanteEdit,fabricanteEliminar


app_name ="fabricantes"
urlpatterns =[
    
    path ('', index,name ='index'),
    path ('nuevo/', fabricanteCreate, name='fabricanteCreate'),
    path ('actualizar/<int:id_fabricante>', fabricanteEdit, name='fabricanteEdit'),
    path ('eliminar/<int:id_fabricante>', fabricanteEliminar, name='fabricanteEliminar')
]

