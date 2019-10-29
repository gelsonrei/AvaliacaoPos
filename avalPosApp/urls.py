from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('respostas/<str:cod_disc>/<str:slug_aval>/', views.listaRespostasAvaliacaoDisciplina, name='respostas'),
    path('avaliacao/<str:cod_disc>/<str:slug_aval>/', views.avaliacao_lista),
    path('avaliacoes/', views.listaAvaliacaoDisciplina),
    path('enviado/', views.finalizado),
    path('relatorio/<str:hash>/', views.relatorio),

    #path('insere/', views.avaliacao_perguntas_create_view),
]

