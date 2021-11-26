from django.urls import path, include

app_name = "aparatos"

urlpatterns = [
    path('', index, name='index'),
]