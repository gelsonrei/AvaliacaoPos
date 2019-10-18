from django.shortcuts import render
from django.db import models

from .models import Avaliacao, Curso, Disciplina, Pergunta

def avaliacao_lista(request, codDisc):
    #avaliacoes = Avaliacao.objects.all()
    avaliacao = Avaliacao.objects.get(cod_disciplina=codDisc)
    perguntas = avaliacao.pergunta_set.all()
    # for pergunta in perguntas:
    #     print(pergunta.texto)
    #     resposta_lista(request,pergunta)
    # respostas = perguntas.respostas_set.all()
    # print(perguntas)
    context = {'avaliacao':avaliacao,
        'perguntas': perguntas,
    }
    return render(request, 'avalPosApp/avaliacao_lista.html', context)



