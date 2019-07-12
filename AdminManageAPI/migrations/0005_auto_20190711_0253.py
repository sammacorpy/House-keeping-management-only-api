# Generated by Django 2.2.3 on 2019-07-10 21:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminManageAPI', '0004_auto_20190711_0154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='activity',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 2, 53, 27, 901406)),
        ),
        migrations.AlterField(
            model_name='activity',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 2, 53, 27, 901406)),
        ),
        migrations.AlterField(
            model_name='asset',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 2, 53, 27, 901406)),
        ),
        migrations.AlterField(
            model_name='asset',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 2, 53, 27, 901406)),
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField(blank=True, max_length=10, null=True)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2019, 7, 11, 2, 53, 27, 902401))),
                ('updated_on', models.DateTimeField(default=datetime.datetime(2019, 7, 11, 2, 53, 27, 902401))),
                ('skills', models.ManyToManyField(blank=True, to='AdminManageAPI.Skill')),
            ],
        ),
        migrations.AddField(
            model_name='skill',
            name='workers',
            field=models.ManyToManyField(blank=True, to='AdminManageAPI.Worker'),
        ),
    ]
