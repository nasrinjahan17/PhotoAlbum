# Generated by Django 3.2.4 on 2021-06-15 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albumapp', '0006_auto_20210615_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='photo_category',
            new_name='name',
        ),
    ]