# Generated by Django 3.2.4 on 2021-07-07 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elib', '0003_book_pdf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='category',
            new_name='author',
        ),
    ]
