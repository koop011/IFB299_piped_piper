# Generated by Django 2.0.4 on 2018-05-20 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_account', '0014_auto_20180520_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentdata',
            old_name='GenderRadioOptions',
            new_name='Gender',
        ),
    ]