# Generated by Django 3.2.7 on 2021-09-26 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.EmailField(default=True, max_length=254),
        ),
    ]
