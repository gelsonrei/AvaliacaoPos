# Generated by Django 2.2.6 on 2019-10-23 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avalPosApp', '0021_auto_20191022_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opcao',
            name='tipoOpcao',
        ),
    ]
