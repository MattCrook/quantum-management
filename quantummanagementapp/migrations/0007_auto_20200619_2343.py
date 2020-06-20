# Generated by Django 3.0.7 on 2020-06-19 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quantummanagementapp', '0006_auto_20200619_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='is_hourly',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='is_salary',
        ),
        migrations.AddField(
            model_name='employee',
            name='pay_rate',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]