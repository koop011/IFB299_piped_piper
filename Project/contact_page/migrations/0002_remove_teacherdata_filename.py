# Generated by Django 2.0.4 on 2018-04-30 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherdata',
            name='filename',
        ),
    ]
