# Generated by Django 4.1.3 on 2023-03-18 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybbs', '0002_post_comment_count_post_like_count_post_public_range'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Haiku',
            new_name='Seiseki',
        ),
    ]
