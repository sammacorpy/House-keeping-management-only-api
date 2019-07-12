# Generated by Django 2.2.3 on 2019-07-10 23:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminManageAPI', '0007_auto_20190711_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 5, 20, 13, 818665)),
        ),
        migrations.AlterField(
            model_name='activity',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 5, 20, 13, 818665)),
        ),
        migrations.AlterField(
            model_name='asset',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 5, 20, 13, 818665)),
        ),
        migrations.AlterField(
            model_name='asset',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 5, 20, 13, 818665)),
        ),
        migrations.AlterField(
            model_name='taskassign',
            name='timeOfAllocation',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 5, 20, 13, 819662)),
        ),
        migrations.AlterField(
            model_name='taskassign',
            name='timeToComplete',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 5, 20, 13, 819662)),
        ),
        migrations.AlterField(
            model_name='worker',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 5, 20, 13, 819662)),
        ),
        migrations.AlterField(
            model_name='worker',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 5, 20, 13, 819662)),
        ),
    ]