# Generated by Django 3.2.18 on 2023-04-05 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybbs', '0007_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tags', to='mybbs.Tag'),
        ),
    ]