# Generated by Django 4.1.2 on 2022-11-19 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_message_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='linkedIn',
            field=models.CharField(max_length=200, null=True),
        ),
    ]