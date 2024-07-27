# Generated by Django 5.0.7 on 2024-07-25 17:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lernplatform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answered_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answered_questions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL),
        ),
    ]