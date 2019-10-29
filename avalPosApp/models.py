from django.conf import settings
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class Curso(models.Model):
    cod= models.CharField("Código Curso", max_length=10, primary_key=True)
    titulo= models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return self.cod

class Disciplina(models.Model):
    cod= models.CharField("Código Disciplina", max_length=10, primary_key=True)
    cod_curso= models.ForeignKey(Curso, on_delete=models.CASCADE) 
    titulo= models.CharField(max_length=250,  null=True, blank=True)
    def __str__(self):
        return self.cod

class Avaliacao(models.Model):
    #cod_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE) 
    descricao = models.CharField("Descrição", max_length=1000)
    slug   = models.SlugField( null=True, blank=True, editable=False)
    dt_ini = models.DateTimeField("Inicio",auto_now=False, auto_now_add=False, null=True, blank=True)
    dt_fim = models.DateTimeField("Fim",auto_now=False, auto_now_add=False, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     return f"/avaliacao/{self.cod_disciplina}"

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.descricao)
        super(Avaliacao, self).save(*args, **kwargs)

class Pergunta(models.Model):
    texto = models.CharField(max_length=1000, unique=True)
   
    TIPO_ALTERNATIVAS = [
        ('DC', 'Descritiva'),
        ('ME', 'Múltipla Escolha'),
        ('CS', 'Caixa de Seleção'),
    ]
 
    tipo_resposta = models.CharField(
        max_length=2,
        choices=TIPO_ALTERNATIVAS,
        default='ME',
    )
   
    def publish(self):
        self.save()

    def __str__(self):
        return (self.texto)

class AvaliacaoDisciplina(models.Model): 
    class Meta:
        unique_together = (('avaliacao', 'disciplina'),)
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE) 
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE) 

    def get_absolute_url(self):
        return f"/avaliacao/{self.disciplina}/{self.avaliacao.slug}/"
    def get_respostas_url(self):
        return f"/respostas/{self.disciplina}/{self.avaliacao.slug}/"

class RespostaOpcao(models.Model): 
    texto = models.CharField(max_length=1000, unique=True) 
   
    def __str__(self):
        return self.texto

class AvaliacaoPergunta(models.Model): 
    class Meta:
        unique_together = (('avaliacao', 'pergunta'),)
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE) 
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE) 
    

class PerguntaRespostaOpcao(models.Model): 
    class Meta:
        unique_together = (('pergunta', 'resposta_opcao'),)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE) 
    resposta_opcao = models.ForeignKey(RespostaOpcao, on_delete=models.CASCADE)

class AplicacaoRegistro(models.Model):
    cod_avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    hash_avaliacao  = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pk}"

    def get_absolute_url(self):
        disc = self.disciplina.cod 
        slug = self.cod_avaliacao.slug
        return f"/relatorio/{self.hash_avaliacao}"

class AplicacaoResposta(models.Model):
    id_registro =  models.ForeignKey(AplicacaoRegistro, on_delete=models.CASCADE)
    cod_pergunta =  models.IntegerField()
    texto_pergunta = models.CharField(max_length=1000) 
    texto_resposta = models.CharField(max_length=1000)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id_registro}"

    def get_absolute_url(self):
        return f"/relatorio/{self.id_registro.hash_avaliacao}"

   



    
