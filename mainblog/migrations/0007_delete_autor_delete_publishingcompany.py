# Generated by Django 4.0.3 on 2022-03-28 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0006_remove_project_images'),
    ]

    operations = [
        migrations.DeleteModel(
            name='autor',
        ),
        migrations.DeleteModel(
            name='PublishingCompany',
        ),
    ]
