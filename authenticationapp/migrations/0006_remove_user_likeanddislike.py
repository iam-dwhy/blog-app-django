# Generated by Django 4.1.7 on 2023-04-03 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticationapp', '0005_remove_user_commenting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='LikeAndDislike',
        ),
    ]
