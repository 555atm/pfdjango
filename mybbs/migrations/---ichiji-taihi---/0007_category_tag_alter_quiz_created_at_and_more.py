# Generated by Django 4.1.3 on 2023-03-14 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybbs', '0006_alter_post_options_alter_post_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='quiz',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='投稿日'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='更新日'),
        ),
    ]