# Generated by Django 3.2.7 on 2021-09-26 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=1000)),
                ('summary', models.TextField(default='this is a summary', null=True)),
                ('featured', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('num_employees', models.DecimalField(decimal_places=0, max_digits=1000)),
                ('summary', models.TextField(default='this is a summary', null=True)),
            ],
        ),
    ]
