# Generated by Django 3.2.4 on 2021-11-17 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cos', '0002_menu_card_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default=None, max_length=100)),
                ('last_name', models.CharField(default=None, max_length=100)),
                ('phoneno', models.IntegerField(default=None, max_length=10)),
                ('orderdate', models.CharField(default=None, max_length=50)),
                ('sheduletime', models.CharField(default=None, max_length=50)),
                ('dish_list', models.CharField(default=None, max_length=1000)),
                ('quantity_list', models.CharField(default=None, max_length=1000)),
                ('price_list', models.CharField(default=None, max_length=1000)),
            ],
        ),
    ]