# Generated by Django 4.1.3 on 2023-03-14 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybbs', '0009_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
