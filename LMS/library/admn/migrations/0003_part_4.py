# Generated by Django 3.2.5 on 2021-07-18 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admn', '0002_part_3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part_4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_id', models.IntegerField()),
                ('Book_Name', models.CharField(default='', max_length=75)),
                ('author', models.CharField(default='', max_length=100)),
                ('applicantname', models.CharField(default='None', max_length=50)),
                ('sactime', models.CharField(default='', max_length=10)),
                ('rettime', models.DateTimeField(default='--')),
            ],
        ),
    ]