# Generated by Django 2.1.7 on 2020-01-02 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0011_auto_20200102_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfilesingle',
            name='file',
            field=models.FileField(upload_to='demo/static/upload/'),
        ),
    ]
