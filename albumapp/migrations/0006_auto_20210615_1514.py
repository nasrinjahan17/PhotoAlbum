# Generated by Django 3.2.4 on 2021-06-15 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albumapp', '0005_rename_select_photo_select_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='select_category',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='category',
            name='photo_category',
            field=models.CharField(default=1, max_length=30),
        ),
    ]
