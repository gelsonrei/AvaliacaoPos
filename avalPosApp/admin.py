from django.contrib import admin
from material.admin.decorators import register
from material.admin.options import MaterialModelAdmin
from django.contrib.admin import SimpleListFilter

from .models import Avaliacao,Pergunta, Curso, Disciplina, RespostaOpcao, AvaliacaoPergunta, PerguntaRespostaOpcao, AvaliacaoDisciplina, AplicacaoRegistro, AplicacaoResposta


@register(Curso)
class CursoAdmin(MaterialModelAdmin):
    icon_name = 'school'
    list_display = ('cod','titulo', 'combina_cod_titulo')
    list_display_links = ('cod','titulo', 'combina_cod_titulo' )
    search_fields = ('cod','titulo')
    
    fieldsets = (
        (None, { 
            'fields':(
                'cod',
                'titulo'
            )
        }),
    )

    def combina_cod_titulo(self,obj):
        return "{} - {}".format(obj.cod, obj.titulo)

@register(Disciplina)
class DisciplinaAdmin(MaterialModelAdmin):
    icon_name = 'class'
    list_display = ('cod','cod_curso', 'titulo', 'combina_cod_titulo')
    list_display_links = ('cod','titulo', 'combina_cod_titulo' )
    search_fields = ('cod','cod_curso',)
    fieldsets = (
        (None, { 
            'fields':(
                'cod',
                'cod_curso',
                'titulo'
            )
        }),
    )

    def combina_cod_titulo(self,obj):
        return "{} - {}".format(obj.cod, obj.titulo)

@register(Avaliacao)
class AvaliacaoAdmin(MaterialModelAdmin):
    icon_name = 'assignment'
    
    list_display = ('descricao','dt_ini', 'dt_fim', 'slug')
    list_display_links = ('descricao','dt_ini', 'dt_fim','slug')
    fieldsets = (
        (None, { 
            'fields':(
                'descricao',
                'dt_ini',
                'dt_fim',
            )
        }),
    )

    # def get_cod_curso(self,obj):
    #     cod_curso = Disciplina.objects.get(cod=obj.cod_disciplina).cod_curso
    #     titulo_curso = Curso.objects.get(cod=cod_curso).titulo
    #     return "{} - {}".format(cod_curso, titulo_curso)



@register(Pergunta)
class PerguntaAdmin(MaterialModelAdmin):
    
    icon_name = 'insert_comment'
   
    list_display = ('texto','tipo_resposta')
    list_display_links = ('texto','tipo_resposta')
    #list_filter = ('texto')
    #search_fields = ('texto')
    fieldsets = (
        (None, { 
            'fields':(
                
                'texto',
                'tipo_resposta'
            )
        }),
    )


@register(RespostaOpcao)
class RespostaOpcaoAdmin(MaterialModelAdmin):
    icon_name = 'format_list_numbered'
    #list_display = ('texto','get_pergunta')
    #list_display_links = ('texto')
   
    # fieldsets = (
    #     (None, { 
    #         'fields':(
    #             'texto',
    #             'pergunta'
    #         )
    #     }),
    # )


@register(AvaliacaoDisciplina)
class AvaliacaoDisciplinaAdmin(MaterialModelAdmin):
    list_display = ('avaliacao','disciplina')
    fieldsets = (
        (None, { 
            'fields':(
                'disciplina',
                'avaliacao'
            )
        }),
    )



@register(AvaliacaoPergunta)
class AvaliacaoPerguntaAdmin(MaterialModelAdmin):
    list_display = ('avaliacao','pergunta')
    fieldsets = (
        (None, { 
            'fields':(
                'pergunta',
                'avaliacao'
            )
        }),
    )


# class InLineOpcao(admin.TabularInline):
#      model = RespostaOpcao


@register(PerguntaRespostaOpcao)
class PerguntaRespostaOpcaoAdmin(MaterialModelAdmin):
    list_display = ('pergunta','resposta_opcao')
    #inlines = [InLineOpcao]
    fieldsets = (
        (None, { 
            'fields':(
                'pergunta',
                'resposta_opcao'
            )
        }),
    )

@register(AplicacaoRegistro)
class AplicacaoRegistroAdmin(MaterialModelAdmin):
    icon_name ='reorder'
    list_display = ('pk','cod_avaliacao','hash_avaliacao')
    list_display_links = ('cod_avaliacao','hash_avaliacao')
    fieldsets = (
        (None, { 
            'fields':(
                'pk'
                'cod_avaliacao',
                'hash_avaliacao'
            )
        }),
    )

@register(AplicacaoResposta)
class AplicacaoRespostaAdmin(MaterialModelAdmin):
    icon_name ='question_answer'
    list_display = ('id_registro','cod_pergunta','texto_pergunta','texto_resposta')
    list_display_links = ('cod_pergunta','texto_pergunta','texto_resposta')
    list_filter = ('texto_pergunta','texto_resposta')
    fieldsets = (
        (None, { 
            'fields':(
                'id_registro',
                'cod_pergunta',
                'texto_pergunta',
                'texto_resposta'
            )
        }),
    )

    