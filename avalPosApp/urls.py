from django.urls import path
from . import views

urlpatterns = [
    path('', views.avaliacao_lista, name='avaliacao_lista'),
    path('avaliacao/<str:codDisc>/', views.avaliacao_lista),
]