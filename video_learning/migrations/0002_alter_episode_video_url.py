# Generated by Django 4.2.4 on 2023-09-14 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_learning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='video_url',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
