# Generated by Django 3.0.7 on 2020-06-20 00:20

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quantummanagementapp', '0009_auto_20200620_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='compensation',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='USD', max_digits=6, null=True),
        ),
    ]