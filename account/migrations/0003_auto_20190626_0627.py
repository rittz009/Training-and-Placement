# Generated by Django 2.2.2 on 2019-06-26 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190625_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentdashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('course', models.CharField(max_length=20)),
                ('sem', models.IntegerField()),
                ('department', models.TextField(max_length=30)),
                ('email', models.EmailField(max_length=20)),
                ('mobno', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.CharField(max_length=20),
        ),
    ]
