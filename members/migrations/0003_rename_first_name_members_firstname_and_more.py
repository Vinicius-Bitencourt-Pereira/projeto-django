# Generated by Django 4.1.1 on 2022-09-11 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_rename_firs_name_members_first_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='last_name',
            new_name='lastname',
        ),
    ]
