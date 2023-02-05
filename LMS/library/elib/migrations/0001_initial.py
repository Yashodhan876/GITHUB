# Generated by Django 3.2.4 on 2021-07-06 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_id', models.IntegerField()),
                ('Book_Name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=30)),
                ('ISBN_10', models.CharField(default='', max_length=12)),
                ('desc', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
