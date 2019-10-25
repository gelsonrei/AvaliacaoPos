from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('avaliacao/<str:cod_disc>/<str:slug_aval>/', views.avaliacao_lista),
    path('enviado/', views.finalizado),
    path('relatorio/<str:cod_disc>/<str:slug_aval>/', views.relatorio),

    #path('insere/', views.avaliacao_perguntas_create_view),
]