# Generated by Django 3.0.7 on 2020-06-18 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quantummanagementapp', '0002_auto_20200615_2321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='admin_user_id',
            new_name='admin_user',
        ),
    ]
