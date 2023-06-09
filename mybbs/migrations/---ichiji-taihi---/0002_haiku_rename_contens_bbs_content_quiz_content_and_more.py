# Generated by Django 4.1.3 on 2022-12-21 05:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mybbs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Haiku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='bbs',
            old_name='contens',
            new_name='content',
        ),
        migrations.AddField(
            model_name='quiz',
            name='content',
            field=models.TextField(blank=True, verbose_name='内容'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='投稿日'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=128, verbose_name='タイトル'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='更新日'),
            preserve_default=False,
        ),
    ]
