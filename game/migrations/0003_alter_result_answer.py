# Generated by Django 5.0.6 on 2024-06-12 21:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_alter_result_id_alter_result_quiz_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='game.answer', verbose_name='Resposta'),
        ),
    ]
