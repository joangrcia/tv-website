# Generated by Django 4.2.4 on 2023-08-29 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qn_settings', '0010_rename_iamge_account_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='profile_image',
        ),
    ]
