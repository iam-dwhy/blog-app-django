# Generated by Django 4.1.7 on 2023-04-03 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticationapp', '0004_alter_user_likeanddislike_alter_user_about_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='commenting',
        ),
    ]
