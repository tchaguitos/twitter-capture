# Generated by Django 2.1.5 on 2019-03-06 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190305_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='geo',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='place',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='url',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='verified',
            field=models.BooleanField(default=False, null=True),
        ),
    ]