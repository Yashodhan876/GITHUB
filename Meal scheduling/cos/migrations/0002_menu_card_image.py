# Generated by Django 3.2.4 on 2021-11-08 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_card',
            name='image',
            field=models.ImageField(default='', upload_to='cos/images'),
        ),
    ]