# Generated by Django 3.2.18 on 2023-05-16 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhaiku', '0003_alter_haiku_naka_random'),
    ]

    operations = [
        migrations.RenameField(
            model_name='haiku',
            old_name='kaminoku',
            new_name='kami_go',
        ),
        migrations.RenameField(
            model_name='haiku',
            old_name='nakanoku',
            new_name='naka_shichi',
        ),
        migrations.RenameField(
            model_name='haiku',
            old_name='shimonoku',
            new_name='shimo_go',
        ),
    ]
