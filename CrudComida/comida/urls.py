from django.urls import path
from .views import list_comida, create_comida, update_comida, delete_comida

urlpatterns = [
    path('', list_comida, name='List_comida'),
    path('new', create_comida, name='create_comida'),
    path('update/<int:id>/', update_comida, name='update_comida'),
    path('delete/<int:id>/', delete_comida, name='delete_comida'),
]
