# Generated by Django 4.2.4 on 2023-09-15 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0003_purchase_is_confirmed_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='proof_of_payment',
            field=models.FileField(blank=True, null=True, upload_to='proof_of_payments/'),
        ),
    ]
