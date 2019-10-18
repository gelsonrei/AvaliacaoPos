from django.conf import settings
from django.db import models
from django.utils import timezone


class Curso(models.Model):
    cod= models.CharField("Codigo Curso", default="ABC123",max_length=10, primary_key=True)
    titulo= models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return self.cod

class Disciplina(models.Model):
    cod= models.CharField("Codigo Disciplina",  default="ABC123",max_length=10, primary_key=True)
    cod_curso= models.ForeignKey(Curso,default="ABC123", on_delete=models.CASCADE) 
    titulo= models.CharField(max_length=250,  null=True, blank=True)
    def __str__(self):
        return self.cod

class Avaliacao(models.Model):
    cod_disciplina = models.ForeignKey(Disciplina,default="DXX123", on_delete=models.CASCADE) 
    dt_ini = models.DateTimeField("Inicio",auto_now=False, auto_now_add=False, null=True, blank=True)
    dt_fim = models.DateTimeField("Fim",auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Avaliacao da disciplina %s" %(self.cod_disciplina)

class Pergunta(models.Model):
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE)
    texto = models.CharField(max_length=1000)
    TIPO_ALTERNATIVAS = [
        ('DC', 'Descritiva'),
        ('ME', 'Múltipla Escolha'),
        ('CS', 'Caixa de Seleção'),
    ]
    tipoResposta = models.CharField(
        max_length=2,
        choices=TIPO_ALTERNATIVAS,
        default='ME',
    )

   
    def publish(self):
        self.save()

    def __str__(self):
        return (self.texto)


class Resposta(models.Model):
    cod_pergunta =  models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=1000) 
    def __str__(self):
        return self.texto