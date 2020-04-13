# Generated by Django 3.0.1 on 2020-03-30 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0008_userprofile_uin_code'),
        ('HuntersDen', '0017_den_next_riddle_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hunter_den_mapping',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.UserProfile'),
        ),
    ]