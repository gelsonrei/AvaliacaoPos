# Generated by Django 2.2.6 on 2019-10-25 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avalPosApp', '0034_auto_20191025_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
