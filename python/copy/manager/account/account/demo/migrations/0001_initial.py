# Generated by Django 2.1.7 on 2019-12-16 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('password', models.TextField(max_length=32)),
                ('permissions', models.TextField(blank=True, null=True, verbose_name='permissions')),
                ('email', models.EmailField(max_length=32)),
            ],
            options={
                'permissions': (('admin', '管理员'), ('manager', '项目组'), ('personal', '个人')),
                'default_permissions': (),
            },
        ),
    ]