# Generated by Django 2.2.6 on 2019-10-22 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avalPosApp', '0015_resposta_resposta_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resposta',
            name='resposta_user',
        ),
        migrations.AddField(
            model_name='avaliacaoresposta',
            name='texto',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
