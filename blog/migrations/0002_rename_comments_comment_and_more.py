# Generated by Django 5.0.2 on 2024-03-04 07:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='comments',
            new_name='comment',
        ),
        migrations.RenameIndex(
            model_name='comment',
            new_name='blog_commen_created_4e025c_idx',
            old_name='blog_commen_created_af32ba_idx',
        ),
    ]