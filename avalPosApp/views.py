from django.shortcuts import render
from django.db import models
import hashlib
import datetime
import random

from .models import Avaliacao, Curso, Disciplina, Pergunta, AvaliacaoResposta, Opcao, AvaliacaoRegistro
#from .forms import AvaliacaoRespostasModelForm


# def avaliacao_perguntas_create_view(request):
#     form = AvaliacaoRespostasModelForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.save()
#         form = AvaliacaoRespostasModelForm()
#     template_name = 'avalPosApp/form.html'
#     context = {'form': form}
#     return render(request, template_name, context)  

def avaliacao_lista(request, codDisc):
    #avaliacoes = Avaliacao.objects.all()
    cod_curso = Disciplina.objects.get(cod=codDisc).cod_curso
    curso_titulo = Curso.objects.get(cod=cod_curso).titulo
    avaliacao = Avaliacao.objects.get(cod_disciplina=codDisc)
    perguntas = avaliacao.pergunta_set.all()

    #form = AvaliacaoRespostasModelForm()

    
    if(request.POST):
        s = curso_titulo + str(cod_curso) + str(avaliacao) + str(datetime.datetime.now()) + str(random.randint(0,1000))
        hash = int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16) 
        print(hash)
        avaliacao_registro = AvaliacaoRegistro(cod_avaliacao=avaliacao,hash_avaliacao=hash)
        avaliacao_registro.save()
        #print(request.POST)
        #print(request.POST.getlist('11'))
        for key in request.POST:
            if (key!='csrfmiddlewaretoken'):
                #value = request.POST[key]
                value = request.POST.getlist(key)
                txt_pergunta = Pergunta.objects.get(pk=int(key)).texto

                # print(int(key))
                # print(value)
                # print(len(value))
                # sz = len(value) 
                # if (sz == 1):
                #     value = request.POST(key)
                for v in value:
                    reg = AvaliacaoResposta(
                        #cod_curso=cod_curso,
                        #cod_disciplina=codDisc,
                        #cod_avaliacao=avaliacao,
                        id_registro = avaliacao_registro,
                        texto_pergunta = txt_pergunta, 
                        cod_pergunta = int(key),
                        texto_resposta = v
                    )
                    reg.save()
               


    # form = AvaliacaoRespostasModelForm(request.POST or None, request.FILES or None)
    # if form.is_valid():
    #     obj = form.save(commit=False)
    #     obj.save()
    #     form = AvaliacaoRespostasModelForm()
    template_name = 'avalPosApp/avaliacao_lista.html'
    
    context = {'avaliacao':avaliacao,
        'cod_curso': cod_curso,
        'curso':curso_titulo,
        'perguntas': perguntas,
        #'form': form,
    }
    return render(request, template_name, context)

def home(request):
    #avaliacoes = Avaliacao.objects.all()
    avaliacao = Avaliacao.objects.all()

    context = {'avaliacoes':avaliacao
    }
    return render(request, 'avalPosApp/home.html', context)

