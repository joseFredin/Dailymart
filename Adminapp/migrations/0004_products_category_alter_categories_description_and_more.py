# Generated by Django 5.0.1 on 2024-03-04 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0003_alter_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='Category',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='categories',
            name='Description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='categories',
            name='Name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='Name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='Price',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='Quantity',
            field=models.CharField(max_length=200),
        ),
    ]
