# Generated by Django 3.2.8 on 2021-10-24 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_remove_customer_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=1000000),
        ),
    ]
