# Generated by Django 3.2.5 on 2021-07-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admn', '0003_part_4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part_4',
            name='rettime',
            field=models.DateTimeField(),
        ),
    ]