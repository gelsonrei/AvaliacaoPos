# Generated by Django 2.2.6 on 2019-10-21 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avalPosApp', '0009_teste'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Teste',
        ),
        migrations.AddField(
            model_name='avaliacaorespostas',
            name='resposta_conteudo',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]