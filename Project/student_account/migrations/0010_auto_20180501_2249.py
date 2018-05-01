# Generated by Django 2.0.4 on 2018-05-01 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_account', '0009_auto_20180501_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdata',
            name='UserName',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='GenderRadioOptions',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=5),
        ),
    ]