# Generated by Django 3.0.7 on 2020-06-19 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quantummanagementapp', '0005_employee_park'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='admin_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quantummanagementapp.AdminUser'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_hourly',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_salary',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='park',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='quantummanagementapp.Park'),
        ),
    ]