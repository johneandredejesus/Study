# Generated by Django 3.2.5 on 2021-08-01 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0005_auto_20210801_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personagemmodel',
            name='livro',
        ),
        migrations.AddField(
            model_name='personagemmodel',
            name='livros',
            field=models.ManyToManyField(to='livros.LivroModel'),
        ),
        migrations.CreateModel(
            name='ComprarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livros', to='livros.livromodel')),
            ],
        ),
    ]
