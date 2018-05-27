# Generated by Django 2.0.4 on 2018-05-26 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessonBooking', '0005_cello_clarinet_drums_flute_guitar_keyboard_piano_saxophone_violin'),
    ]

    operations = [
        migrations.CreateModel(
            name='guitar_half_hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='guitar_hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='keyboard_half_hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='keyboard_hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='piano_half_hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='piano_hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='saxophone_half_hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='saxophone_hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='violin_half_hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='violin_hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.TimeField()),
            ],
        ),
        migrations.RenameModel(
            old_name='piano',
            new_name='cello_half_hour',
        ),
        migrations.RenameModel(
            old_name='flute',
            new_name='cello_hour',
        ),
        migrations.RenameModel(
            old_name='clarinet',
            new_name='clarinet_half_hour',
        ),
        migrations.RenameModel(
            old_name='cello',
            new_name='clarinet_hour',
        ),
        migrations.RenameModel(
            old_name='drums',
            new_name='drums_half_hour',
        ),
        migrations.RenameModel(
            old_name='guitar',
            new_name='drums_hour',
        ),
        migrations.RenameModel(
            old_name='keyboard',
            new_name='electric_guitar_half_hour',
        ),
        migrations.RenameModel(
            old_name='violin',
            new_name='flute_half_hour',
        ),
        migrations.RenameModel(
            old_name='saxophone',
            new_name='flute_hour',
        ),
    ]
