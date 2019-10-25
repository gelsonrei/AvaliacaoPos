# Generated by Django 2.2.6 on 2019-10-24 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avalPosApp', '0025_auto_20191024_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respostaopcao',
            name='cod_pergunta',
        ),
        migrations.RemoveField(
            model_name='pergunta',
            name='avaliacao',
        ),
        migrations.AddField(
            model_name='pergunta',
            name='avaliacao',
            field=models.ManyToManyField(to='avalPosApp.Avaliacao'),
        ),
        migrations.CreateModel(
            name='AvaliacaoPergunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avalPosApp.Avaliacao')),
                ('cod_pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avalPosApp.Pergunta')),
            ],
        ),
    ]
