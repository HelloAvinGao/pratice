# Generated by Django 3.0.7 on 2020-06-29 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='telephone',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=6),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='image/2018/05/default_middile_2.png', upload_to='image/%Y/%m'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='手机'),
        ),
    ]
