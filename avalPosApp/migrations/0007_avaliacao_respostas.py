# Generated by Django 2.2.6 on 2019-10-21 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avalPosApp', '0006_remove_avaliacao_cod_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao_Respostas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.CharField(max_length=1000)),
                ('tipoResposta', models.CharField(choices=[('DC', 'Descritiva'), ('ME', 'Múltipla Escolha'), ('CS', 'Caixa de Seleção')], default='ME', max_length=2)),
                ('cod_pergunta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='avalPosApp.Pergunta')),
            ],
        ),
    ]