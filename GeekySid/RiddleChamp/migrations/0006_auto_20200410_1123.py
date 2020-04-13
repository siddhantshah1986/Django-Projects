# Generated by Django 3.0.1 on 2020-04-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiddleChamp', '0005_auto_20200410_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='riddle',
            name='max_calls',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='riddlelevel',
            name='kills',
            field=models.FloatField(default=50.0),
        ),
    ]
