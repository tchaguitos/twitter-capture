# Generated by Django 2.1.5 on 2019-03-06 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_tweet_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='user',
            name='screen_name',
            field=models.CharField(max_length=300),
        ),
    ]