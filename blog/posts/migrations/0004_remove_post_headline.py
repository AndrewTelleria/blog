# Generated by Django 2.0.2 on 2018-02-20 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180220_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='headline',
        ),
    ]