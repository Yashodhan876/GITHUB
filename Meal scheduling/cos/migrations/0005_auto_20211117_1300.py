# Generated by Django 3.2.4 on 2021-11-17 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cos', '0004_order_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='dish_list',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='members',
            field=models.IntegerField(default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderdate',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='phoneno',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='price_list',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity_list',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='sheduletime',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
