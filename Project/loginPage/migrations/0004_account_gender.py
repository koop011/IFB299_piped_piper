# Generated by Django 2.0.4 on 2018-04-29 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginPage', '0003_remove_student_instrument'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.CharField(default='none', max_length=10),
        ),
    ]
