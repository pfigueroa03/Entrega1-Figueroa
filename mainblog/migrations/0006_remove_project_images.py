# Generated by Django 4.0.1 on 2022-03-14 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0005_alter_publishingcompany_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='images',
        ),
    ]
