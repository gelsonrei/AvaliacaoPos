from django.contrib import admin
from .models import Avaliacao, Pergunta, Curso, Disciplina, Resposta, AvaliacaoResposta, Opcao,AvaliacaoRegistro

admin.site.register(Avaliacao)
admin.site.register(Pergunta)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Resposta)
admin.site.register(Opcao)
admin.site.register(AvaliacaoResposta)
admin.site.register(AvaliacaoRegistro)
