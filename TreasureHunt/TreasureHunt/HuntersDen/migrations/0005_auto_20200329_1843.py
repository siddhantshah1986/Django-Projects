# Generated by Django 3.0.1 on 2020-03-29 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HuntersDen', '0004_auto_20200329_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='den',
            name='ended_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]