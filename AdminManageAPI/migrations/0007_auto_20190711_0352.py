# Generated by Django 2.2.3 on 2019-07-10 22:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminManageAPI', '0006_auto_20190711_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 3, 52, 2, 27335)),
        ),
        migrations.AlterField(
            model_name='activity',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 3, 52, 2, 27335)),
        ),
        migrations.AlterField(
            model_name='asset',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 3, 52, 2, 27335)),
        ),
        migrations.AlterField(
            model_name='asset',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 3, 52, 2, 27335)),
        ),
        migrations.AlterField(
            model_name='worker',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 3, 52, 2, 28332)),
        ),
        migrations.AlterField(
            model_name='worker',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 3, 52, 2, 28332)),
        ),
        migrations.CreateModel(
            name='TaskAssign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeOfAllocation', models.DateTimeField(default=datetime.datetime(2019, 7, 11, 3, 52, 2, 28332))),
                ('timeToComplete', models.DateTimeField(default=datetime.datetime(2019, 7, 11, 3, 52, 2, 28332))),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminManageAPI.Asset')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminManageAPI.Activity')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminManageAPI.Worker')),
            ],
        ),
    ]
