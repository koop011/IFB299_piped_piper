# Generated by Django 2.0.4 on 2018-05-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessonBooking', '0010_days'),
    ]

    operations = [
        migrations.CreateModel(
            name='period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('months', models.CharField(default='none', max_length=10)),
            ],
        ),
    ]
