# Generated by Django 2.2.6 on 2019-10-22 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avalPosApp', '0017_auto_20191022_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacaoresposta',
            name='cod_pergunta',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='resposta',
            name='cod_pergunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avalPosApp.Pergunta'),
        ),
    ]