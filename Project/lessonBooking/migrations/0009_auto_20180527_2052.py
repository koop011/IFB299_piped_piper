# Generated by Django 2.0.4 on 2018-05-27 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessonBooking', '0008_auto_20180527_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='pendinglessoncontracts',
            name='first_name',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='pendinglessoncontracts',
            name='instrument',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='pendinglessoncontracts',
            name='last_name',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='pendinglessoncontracts',
            name='time',
            field=models.TimeField(default='00:00:00'),
        ),
    ]