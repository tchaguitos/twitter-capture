# Generated by Django 2.1.5 on 2019-03-06 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_tweet_credated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]