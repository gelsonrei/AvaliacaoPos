# Generated by Django 2.2.6 on 2019-10-23 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avalPosApp', '0022_remove_opcao_tipoopcao'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Resposta',
            new_name='RespostaOpcao',
        ),
    ]
