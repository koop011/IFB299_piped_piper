# Generated by Django 2.0.4 on 2018-05-23 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_page', '0008_teacherdata_electric_guitar'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherdata',
            name='guitar',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='teacherdata',
            name='keyboard',
            field=models.BooleanField(default='False'),
        ),
    ]