# Generated by Django 2.0.4 on 2018-05-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lessonBooking', '0002_delete_violinhourtimes'),
    ]

    operations = [
        migrations.CreateModel(
            name='electric_guitar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.TimeField()),
            ],
        ),
    ]
