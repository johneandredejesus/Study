# Generated by Django 3.2.5 on 2021-08-01 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livromodel',
            name='autor',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='livromodel',
            name='isbn',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='livromodel',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='personagemmodel',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
