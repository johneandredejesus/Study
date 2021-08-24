# Generated by Django 3.2.5 on 2021-08-01 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0008_alter_capamodel_livro'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComprarLivroModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('livro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='livros', to='livros.livromodel')),
            ],
        ),
        migrations.AlterField(
            model_name='capamodel',
            name='livro',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='livro', to='livros.livromodel'),
        ),
        migrations.DeleteModel(
            name='ComprarModel',
        ),
    ]
