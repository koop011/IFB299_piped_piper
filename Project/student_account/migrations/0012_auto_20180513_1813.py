# Generated by Django 2.0.4 on 2018-05-13 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_account', '0011_auto_20180503_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='GenderRadioOptions',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=7),
        ),
    ]