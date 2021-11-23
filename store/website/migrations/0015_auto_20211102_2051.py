# Generated by Django 3.2.8 on 2021-11-03 00:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0014_remove_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='eyw_transactionref',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]