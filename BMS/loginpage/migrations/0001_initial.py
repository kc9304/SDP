# Generated by Django 4.2.4 on 2023-09-05 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'login_table',
            },
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=150, unique=True)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('dateofbirth', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Signup_table',
            },
        ),
    ]