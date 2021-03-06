# Generated by Django 3.2.5 on 2021-08-01 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0011_auto_20210801_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capa',
            old_name='frete',
            new_name='frente',
        ),
        migrations.AlterField(
            model_name='capa',
            name='livro',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='capas', to='livros.livro'),
        ),
    ]
