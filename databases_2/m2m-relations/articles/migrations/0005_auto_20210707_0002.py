# Generated by Django 3.1.2 on 2021-07-06 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20210707_0000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relationship',
            old_name='tag',
            new_name='topic',
        ),
    ]
