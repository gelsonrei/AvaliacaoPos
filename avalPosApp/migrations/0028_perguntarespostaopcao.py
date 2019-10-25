# Generated by Django 2.2.6 on 2019-10-24 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avalPosApp', '0027_respostaopcao_pergunta'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerguntaRespostaOpcao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avalPosApp.Pergunta')),
                ('cod_resposta_opcao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avalPosApp.RespostaOpcao')),
            ],
        ),
    ]
