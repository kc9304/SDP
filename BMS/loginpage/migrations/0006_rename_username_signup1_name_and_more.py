# Generated by Django 4.2.4 on 2023-10-12 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0005_rename_email_signup1_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup1',
            old_name='username',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='signup1',
            old_name='password',
            new_name='psw',
        ),
    ]
