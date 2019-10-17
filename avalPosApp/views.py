from django.shortcuts import render
from .models import Avaliacao, Curso, Disciplina, Pergunta

def avaliacao_lista(request):
    avaliacoes = Avaliacao.objects.all()
    context = {'avaliacoes':avaliacoes}
    return render(request, 'avalPosApp/avaliacao_lista.html', context)
