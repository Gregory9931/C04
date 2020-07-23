# Generated by Django 3.0.3 on 2020-07-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_crawlrequest_antiblock_use_user_agents'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crawlrequest',
            old_name='antiblock_cookies_file',
            new_name='antiblock_cookies_user_defined',
        ),
        migrations.RemoveField(
            model_name='crawlrequest',
            name='antiblock_mask_type',
        ),
        migrations.AddField(
            model_name='crawlrequest',
            name='antiblock_cookies_management_type',
            field=models.CharField(blank=True, choices=[('default', 'Default'), ('user-defined', 'User defined cookies')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='crawlrequest',
            name='antiblock_use_ip_rotation',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]