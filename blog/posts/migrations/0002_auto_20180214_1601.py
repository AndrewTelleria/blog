# Generated by Django 2.0.2 on 2018-02-15 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_mod',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_pub',
            field=models.DateField(blank=True, null=True),
        ),
    ]