# Generated by Django 2.2.2 on 2019-07-01 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_studentdashboard_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_teacher',
        ),
    ]