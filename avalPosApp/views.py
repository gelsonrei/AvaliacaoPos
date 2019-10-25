from django.shortcuts import render, redirect
from django.db import models
import datetime


from .models import Avaliacao, Pergunta, Curso, Disciplina,RespostaOpcao,  AvaliacaoPergunta, PerguntaRespostaOpcao, AvaliacaoDisciplina, AplicacaoRegistro, AplicacaoResposta

def avaliacao_lista(request, cod_disc, slug_aval):
    
    avaliacao = Avaliacao.objects.get(slug = slug_aval)
    avaliacao_descricao = avaliacao.descricao

    cod_curso = Disciplina.objects.get(cod=cod_disc).cod_curso
    curso_titulo = Curso.objects.get(cod=cod_curso).titulo
    disciplina_titulo = Disciplina.objects.get(cod=cod_disc).titulo
    perguntas = AvaliacaoPergunta.objects.all().filter(avaliacao=avaliacao)
    opcoes = PerguntaRespostaOpcao.objects.all()
    
    # for i in perguntas:
    #     print(i.avaliacao)
    #     print(i.pergunta)
    # print(avaliacao)    
    # print(avaliacao_descricao)    
    # print(cod_curso)    
    # print(curso_titulo)    
    # print(disciplina_titulo) 
   
    
    if(request.POST):
        #s = curso_titulo + str(cod_curso) + str(avaliacao) + str(datetime.datetime.now()) + str(random.randint(0,1000))
        #hash = int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16) 
        hash = request.POST['csrfmiddlewaretoken']
        aplicacao_registro = AplicacaoRegistro(cod_avaliacao=avaliacao,hash_avaliacao=hash)
        aplicacao_registro.save()
        #print(request.POST)
        for key in request.POST:
            if (key!='csrfmiddlewaretoken'):
                #value = request.POST[key]
                value = request.POST.getlist(key)
                txt_pergunta = Pergunta.objects.get(pk=int(key)).texto
                print(value)
                for v in value:
                    reg = AplicacaoResposta(
                        id_registro = aplicacao_registro,
                        texto_pergunta = txt_pergunta, 
                        cod_pergunta = int(key),
                        texto_resposta = v
                    )
                    reg.save()
        return redirect("/enviado")
   
    template_name = 'avalPosApp/avaliacao_lista.html'
    context = {}
    
    context = {
        'avaliacao':avaliacao,
        'cod_curso': cod_curso,
        'curso':curso_titulo,
        'cod_disciplina': cod_disc,
        'disciplina': disciplina_titulo,
        'perguntas': perguntas,
        'opcoes': opcoes
    }
    return render(request, template_name, context)

def home(request):
    avaliacao = AvaliacaoDisciplina.objects.all()

    context = {
        'avaliacoes':avaliacao
    }
    return render(request, 'avalPosApp/home.html', context)

def finalizado(request):
    return render(request, 'avalPosApp/final.html', {})