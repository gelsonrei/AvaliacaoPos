# Generated by Django 2.2.6 on 2019-10-24 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avalPosApp', '0029_auto_20191024_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pergunta',
            name='avaliacao',
        ),
        migrations.RemoveField(
            model_name='respostaopcao',
            name='pergunta',
        ),
    ]