# Generated by Django 3.1.4 on 2020-12-17 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('aadhar_number', models.IntegerField(primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=200)),
                ('zone', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('occupation', models.CharField(default='None', max_length=200)),
                ('isatRisk', models.BooleanField(default=False)),
            ],
        ),
    ]
