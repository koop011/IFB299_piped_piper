# Generated by Django 2.0.4 on 2018-05-16 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_page', '0005_auto_20180516_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherdata',
            name='file',
        ),
    ]
