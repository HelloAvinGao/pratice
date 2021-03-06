# Generated by Django 3.0.7 on 2020-06-29 03:40

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=50)),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
            ],
            managers=[
                ('permission', django.db.models.manager.Manager()),
            ],
        ),
    ]
