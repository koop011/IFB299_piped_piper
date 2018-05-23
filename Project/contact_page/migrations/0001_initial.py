# Generated by Django 2.0.4 on 2018-04-30 16:02


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=200)),
                ('DoB', models.CharField(default='none', max_length=20)),
                ('HomeAddress', models.CharField(default='none', max_length=200)),
                ('email', models.CharField(default='none', max_length=200)),
                ('pNumber', models.CharField(default='none', max_length=13)),
                ('certificates', models.CharField(default='none', max_length=200)),
                ('subjects', models.CharField(default='none', max_length=200)),
                ('filename', models.FileField(upload_to='')),
            ],
        ),
    ]
