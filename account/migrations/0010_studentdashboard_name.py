# Generated by Django 2.2.2 on 2019-07-01 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_account_is_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdashboard',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
