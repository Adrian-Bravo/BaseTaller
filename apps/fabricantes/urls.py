from django.urls import path, include
from apps.fabricantes.views import index

app_name ="fabricantes"
urlpatterns =[
    path ('', index)
]

