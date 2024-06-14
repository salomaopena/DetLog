# Generated by Django 5.0.6 on 2024-06-13 01:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_result_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='max_score',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=10, verbose_name='Pontos máximos'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions_options', to='game.question', verbose_name='Questão'),
        ),
    ]