# Generated by Django 2.2.3 on 2019-07-10 20:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=30)),
                ('properties', models.CharField(blank=True, max_length=100, null=True)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2019, 7, 11, 1, 42, 21, 729761))),
                ('updated_on', models.DateTimeField(default=datetime.datetime(2019, 7, 11, 1, 42, 21, 729761))),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('frequency', models.CharField(choices=[('H', 'Hourly'), ('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly'), ('Y', 'Yearly')], max_length=30)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2019, 7, 11, 1, 42, 21, 730758))),
                ('updated_on', models.DateTimeField(default=datetime.datetime(2019, 7, 11, 1, 42, 21, 730758))),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminManageAPI.Assets')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
