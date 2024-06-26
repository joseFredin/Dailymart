# Generated by Django 5.0.1 on 2024-03-01 05:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkoutdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=200)),
                ('State', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=200)),
                ('Postcode', models.CharField(max_length=200)),
                ('cartid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.cart')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.register')),
            ],
        ),
    ]
