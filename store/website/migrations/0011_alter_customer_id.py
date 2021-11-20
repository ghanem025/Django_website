# Generated by Django 3.2.8 on 2021-10-26 19:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_alter_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
