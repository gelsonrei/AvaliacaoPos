from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('avaliacao/<str:codDisc>/', views.avaliacao_lista),
    path('enviado/', views.finalizado),
    #path('insere/', views.avaliacao_perguntas_create_view),
]