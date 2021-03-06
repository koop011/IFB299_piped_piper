# Generated by Django 2.0.4 on 2018-05-27 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(default='none', max_length=200)),
                ('LastName', models.CharField(default='none', max_length=200)),
                ('UserName', models.CharField(default='none', max_length=20)),
                ('password', models.CharField(default='none', max_length=20)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=7)),
                ('DoB', models.DateField(blank=True, null=True)),
                ('HomeAddress', models.CharField(default='none', max_length=200)),
                ('Email', models.CharField(default='none', max_length=200)),
                ('pNumber', models.CharField(default='none', max_length=13)),
                ('instrument', models.CharField(default='none', max_length=20)),
                ('pFirstName', models.CharField(default='none', max_length=200)),
                ('pLastName', models.CharField(default='none', max_length=200)),
                ('parentsNumber', models.CharField(default='none', max_length=13)),
                ('pEmail', models.CharField(default='none', max_length=200)),
            ],
        ),
    ]
