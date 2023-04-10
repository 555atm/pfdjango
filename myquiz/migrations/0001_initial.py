# Generated by Django 4.1.3 on 2023-03-29 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('question', models.TextField(blank=True, verbose_name='問題')),
                ('choice_a', models.TextField(blank=True, verbose_name='選択肢a')),
                ('choice_b', models.TextField(blank=True, verbose_name='選択肢b')),
                ('choice_c', models.TextField(blank=True, verbose_name='選択肢c')),
                ('answer', models.TextField(blank=True, verbose_name='答え')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre', to='myquiz.genre', verbose_name='ジャンル')),
            ],
        ),
    ]