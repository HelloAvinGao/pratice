# Generated by Django 2.1.7 on 2020-01-09 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0013_delete_uploadfilesingle'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('password', models.TextField(max_length=32)),
                ('permissions', models.TextField(blank=True, null=True, verbose_name='permissions')),
                ('email', models.EmailField(max_length=32)),
            ],
            options={
                'permissions': (('admin', 'manager the page'), ('manager', 'manager the project'), ('personal', 'personal')),
                'default_permissions': (),
            },
        ),
    ]
