# Generated by Django 2.2.12 on 2020-06-05 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200529_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawlrequest',
            name='obey_robots',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
