# Generated by Django 3.1.2 on 2021-03-11 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0005_auto_20210311_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(default='Your Complaint Registered ', max_length=1000),
        ),
    ]
