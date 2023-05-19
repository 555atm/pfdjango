# Generated by Django 3.2.18 on 2023-05-15 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhaiku', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='haiku',
            name='kami_random',
            field=models.TextField(max_length=64, null=True, verbose_name='上ランダム文字'),
        ),
        migrations.AlterField(
            model_name='haiku',
            name='naka_random',
            field=models.TextField(blank=True, max_length=64, verbose_name='中ランダム文字'),
        ),
        migrations.AlterField(
            model_name='haiku',
            name='shimo_random',
            field=models.TextField(max_length=64, null=True, verbose_name='下ランダム文字'),
        ),
    ]