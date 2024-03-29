# Generated by Django 2.2.6 on 2019-10-25 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avalPosApp', '0042_auto_20191025_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aplicacaoregistro',
            name='cod_avaliacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avalPosApp.Avaliacao'),
        ),
        migrations.AlterField(
            model_name='aplicacaoregistro',
            name='hash_avaliacao',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='aplicacaoresposta',
            name='cod_pergunta',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='aplicacaoresposta',
            name='id_registro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avalPosApp.AplicacaoRegistro'),
        ),
        migrations.AlterField(
            model_name='aplicacaoresposta',
            name='texto_pergunta',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='aplicacaoresposta',
            name='texto_resposta',
            field=models.CharField(max_length=1000),
        ),
    ]
