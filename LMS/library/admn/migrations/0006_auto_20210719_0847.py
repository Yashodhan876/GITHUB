# Generated by Django 3.2.5 on 2021-07-19 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admn', '0005_alter_part_4_rettime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part_2',
            name='applicantname',
        ),
        migrations.AlterField(
            model_name='part_4',
            name='rettime',
            field=models.CharField(default='--', max_length=10),
        ),
    ]
