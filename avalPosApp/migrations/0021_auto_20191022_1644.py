# Generated by Django 2.2.6 on 2019-10-22 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avalPosApp', '0020_auto_20191022_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacaoresposta',
            name='cod_avaliacao',
        ),
        migrations.RemoveField(
            model_name='avaliacaoresposta',
            name='cod_curso',
        ),
        migrations.RemoveField(
            model_name='avaliacaoresposta',
            name='cod_disciplina',
        ),
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=1000)),
                ('tipoOpcao', models.CharField(choices=[('DC', 'Descritiva'), ('ME', 'Múltipla Escolha'), ('CS', 'Caixa de Seleção')], default='ME', max_length=2)),
                ('cod_pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avalPosApp.Pergunta')),
            ],
        ),
        migrations.CreateModel(
            name='AvaliacaoRegistro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_avaliacao', models.CharField(max_length=100)),
                ('cod_avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avalPosApp.Avaliacao')),
            ],
        ),
        migrations.AddField(
            model_name='avaliacaoresposta',
            name='id_registro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='avalPosApp.AvaliacaoRegistro'),
            preserve_default=False,
        ),
    ]
