# Generated by Django 2.0.4 on 2018-04-30 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_account', '0005_auto_20180501_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdata',
            name='GenderRadioOptions',
        ),
    ]
