from django.shortcuts import render, redirect
from django.db import models
from django.db.models import Q
import datetime


from .models import Avaliacao, Pergunta, Curso, Disciplina,RespostaOpcao,  AvaliacaoPergunta, PerguntaRespostaOpcao, AvaliacaoDisciplina, AplicacaoRegistro, AplicacaoResposta

def avaliacao_lista(request, cod_disc, slug_aval):
    
    avaliacao = Avaliacao.objects.get(slug = slug_aval)
    avaliacao_descricao = avaliacao.descricao

    cod_curso = Disciplina.objects.get(cod=cod_disc).cod_curso
    curso_titulo = Curso.objects.get(cod=cod_curso).titulo
    
    disciplina = Disciplina.objects.get(cod=cod_disc)
    disciplina_titulo = disciplina.titulo
    
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
        aplicacao_registro = AplicacaoRegistro(cod_avaliacao=avaliacao,hash_avaliacao=hash,disciplina=disciplina)
        aplicacao_registro.save()
        #print(request.POST)
        for key in request.POST:
            if (key!='csrfmiddlewaretoken'):
                #value = request.POST[key]
                value = request.POST.getlist(key)
                txt_pergunta = Pergunta.objects.get(pk=int(key)).texto
                print(len(value))
                reg = AplicacaoResposta(
                        id_registro = aplicacao_registro,
                        texto_pergunta = txt_pergunta, 
                        cod_pergunta = int(key),
                        texto_resposta = ""
                    )

                resp = ""
                if (len(value)>1):
                    for v in value:
                        resp=resp+v+"; "
                else:
                    resp = value[0]

                reg.texto_resposta = resp

                # for v in value:
                #     reg = AplicacaoResposta(
                #         id_registro = aplicacao_registro,
                #         texto_pergunta = txt_pergunta, 
                #         cod_pergunta = int(key),
                #         texto_resposta = v
                #     )
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


def relatorio(request, hash):
    registro = AplicacaoRegistro.objects.get(hash_avaliacao=hash)
    respostas = AplicacaoResposta.objects.filter(id_registro=registro).order_by('cod_pergunta')
   
    # print(registro.cod_avaliacao)
    # print(registro.disciplina)
    # print(respostas)
    # context = {}

    context = {
        'registro' : registro,
        'respostas':respostas
    }
    return render(request, 'avalPosApp/relatorio.html', context)

def home(request):
    avaliacao = AvaliacaoDisciplina.objects.all()

    context = {
        'avaliacoes':avaliacao
    }
    return render(request, 'avalPosApp/home.html', context)

def listaRespostas(request):
    aplicacao_registro = AplicacaoRegistro.objects.all()
   
    context = {
        'registros': aplicacao_registro
    }
    return render(request, 'avalPosApp/respostas_lista.html', context)

def listaAvaliacaoDisciplina(request):
   
    avaliacaoDisciplina = AvaliacaoDisciplina.objects.all()
   
    context = {
        'avaliacaoDisciplina': avaliacaoDisciplina
    }
    return render(request, 'avalPosApp/avaliacoes.html', context)

def listaRespostasAvaliacaoDisciplina(request, slug_aval, cod_disc):

    avaliacao = Avaliacao.objects.get(slug=slug_aval)
    disciplina = Disciplina.objects.get(cod = cod_disc)

    aplicacaoRegistro = AplicacaoRegistro.objects.all().filter(cod_avaliacao=avaliacao, disciplina=disciplina)
    aplicacaoRespostas = AplicacaoResposta.objects.filter(Q(id_registro__in = aplicacaoRegistro))

    perguntas = AvaliacaoPergunta.objects.all().filter(avaliacao=avaliacao)

    for r in aplicacaoRegistro:
        print(r.pk)
    
    
    for p in perguntas:
        print(p.pergunta.texto)

    # ids = list()
    
    # for p in aplicacaoRegistro:
    #     ids.append(p.pk)
    
    # for i in aplicacaoRespostas:
    #     if (i.id_registro.pk in ids):
    #         print(i.id_registro)
    
    # print(aplicacaoRespostas)
   
    context = {
        'perguntas':perguntas,
        'avaliacao': avaliacao,
        'disciplina': disciplina,
        'aplicacaoRegistro': aplicacaoRegistro,
        'aplicacaoRespostas': aplicacaoRespostas
    }
    return render(request, 'avalPosApp/respostasPorAvaliacao.html', context)





def finalizado(request):
    return render(request, 'avalPosApp/final.html', {})


