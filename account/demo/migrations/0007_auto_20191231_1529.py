# Generated by Django 2.1.7 on 2019-12-31 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0006_auto_20191231_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkresult',
            name='data',
            field=models.CharField(blank=True, max_length=100000),
        ),
        migrations.AlterField(
            model_name='checkresult',
            name='tableName',
            field=models.CharField(max_length=32),
        ),
    ]
