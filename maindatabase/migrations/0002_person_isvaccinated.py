# Generated by Django 3.1.4 on 2020-12-17 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindatabase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='isVaccinated',
            field=models.BooleanField(default=False),
        ),
    ]
