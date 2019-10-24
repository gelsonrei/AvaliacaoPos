from django.contrib import admin
from material.admin.decorators import register
from material.admin.options import MaterialModelAdmin
from django.contrib.admin import SimpleListFilter

from .models import Avaliacao, Pergunta, Curso, Disciplina, AvaliacaoResposta, RespostaOpcao, AvaliacaoRegistro


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
    
    list_display = ('cod_disciplina','get_cod_curso','dt_ini', 'dt_fim')
    list_display_links = ('cod_disciplina','dt_ini', 'dt_fim')
    fieldsets = (
        (None, { 
            'fields':(
                'cod_disciplina',
                'dt_ini',
                'dt_fim',
            )
        }),
    )

    def get_cod_curso(self,obj):
        cod_curso = Disciplina.objects.get(cod=obj.cod_disciplina).cod_curso
        titulo_curso = Curso.objects.get(cod=cod_curso).titulo
        return "{} - {}".format(cod_curso, titulo_curso)


class InLineRespostas(admin.TabularInline):
    model = RespostaOpcao

@register(Pergunta)
class PerguntaAdmin(MaterialModelAdmin):
    
    icon_name = 'insert_comment'
    inlines = [InLineRespostas]
    list_display = ('avaliacao','get_avaliacao_disciplina','texto','tipo_resposta')
    list_display_links = ('avaliacao','texto','tipo_resposta')
    list_filter = ('avaliacao','texto')
    search_fields = ('get_avaliacao_disciplina','texto')
    fieldsets = (
        (None, { 
            'fields':(
                'avaliacao',
                'texto',
                'tipo_resposta'
            )
        }),
    )

    def get_avaliacao_disciplina(self,obj):
        cod_disciplina = obj.avaliacao.cod_disciplina
        titulo_disciplina  = Disciplina.objects.get(cod=cod_disciplina).titulo
        # avaliacao = Avaliacao.objects.get()
        # cod_curso = Disciplina.objects.get(cod=obj.cod_disciplina).cod_curso
        # titulo_curso = Curso.objects.get(cod=cod_curso).titulo
        return "{} - {}".format(cod_disciplina, titulo_disciplina)





@register(RespostaOpcao)
class RespostaOpcaoAdmin(MaterialModelAdmin):
    icon_name = 'format_list_numbered'
    list_display = ('cod_pergunta','texto')
    list_display_links = ('cod_pergunta','texto')
   
    fieldsets = (
        (None, { 
            'fields':(
                'cod_pergunta',
                'texto'
            )
        }),
    )

@register(AvaliacaoRegistro)
class AvaliacaoRegistroAdmin(MaterialModelAdmin):
    icon_name ='reorder'
    list_display = ('cod_avaliacao','hash_avaliacao')
    list_display_links = ('cod_avaliacao','hash_avaliacao')
    fieldsets = (
        (None, { 
            'fields':(
                'cod_avaliacao',
                'hash_avaliacao'
            )
        }),
    )

@register(AvaliacaoResposta)
class AvaliacaoRespostaAdmin(MaterialModelAdmin):
    icon_name ='question_answer'
    list_display = ('id_registro','cod_pergunta','texto_pergunta','texto_resposta')
    list_display_links = ('id_registro','cod_pergunta','texto_pergunta','texto_resposta')
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

    