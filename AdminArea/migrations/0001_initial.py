# Generated by Django 3.0 on 2021-07-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Registration',
            fields=[
                ('fname', models.CharField(max_length=100)),
                ('mname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('dob', models.DateField(max_length=8)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='', max_length=10)),
                ('aadhar', models.CharField(max_length=12)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=10)),
                ('photo', models.ImageField(default='', upload_to='AdminPhotos/')),
                ('status', models.CharField(default='activated', max_length=100)),
                ('last_login', models.CharField(default='', max_length=100)),
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(default='', max_length=100)),
                ('cpassword', models.CharField(default='', max_length=100)),
                ('sreenpin', models.CharField(default='', max_length=100)),
                ('csreenpin', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
