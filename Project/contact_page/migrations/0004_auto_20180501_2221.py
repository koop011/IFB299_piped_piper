# Generated by Django 2.0.4 on 2018-05-01 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_page', '0003_teacherdata_filename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacherdata',
            old_name='filename',
            new_name='file',
        ),
        migrations.RemoveField(
            model_name='teacherdata',
            name='FullName',
        ),
        migrations.AddField(
            model_name='teacherdata',
            name='fname',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='teacherdata',
            name='lname',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
