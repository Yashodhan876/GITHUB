# Generated by Django 3.2.5 on 2021-07-16 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elib', '0007_auto_20210707_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(default='elib/pdf/Soft_Copy_of_Book_is_Not_Available.pdf', upload_to='elib/pdf'),
        ),
    ]
