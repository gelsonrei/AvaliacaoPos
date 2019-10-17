# Generated by Django 2.2.6 on 2019-10-17 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avalPosApp', '0003_auto_20191017_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='cod_curso',
            field=models.ForeignKey(default='ABC123', on_delete=django.db.models.deletion.CASCADE, to='avalPosApp.Curso'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='cod_disciplina',
            field=models.ForeignKey(default='DXX123', on_delete=django.db.models.deletion.CASCADE, to='avalPosApp.Disciplina'),
        ),
    ]