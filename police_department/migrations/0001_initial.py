# Generated by Django 3.2.15 on 2022-08-15 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calls',
            fields=[
                ('crime_id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='Crime ID')),
                ('crime_type', models.CharField(max_length=150, verbose_name='Crime Type')),
                ('report_date', models.DateTimeField(verbose_name='Report Date')),
                ('call_date', models.DateTimeField(verbose_name='Call Date')),
                ('offense_date', models.DateTimeField(verbose_name='Offense Date')),
                ('call_time', models.CharField(max_length=10, verbose_name='Call Time')),
                ('call_date_time', models.DateTimeField(verbose_name='Call Date Time')),
                ('disposition', models.CharField(max_length=150, verbose_name='Disposition')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('state', models.CharField(max_length=50, verbose_name='State')),
                ('agency_id', models.IntegerField(verbose_name='Agency ID')),
                ('address_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address Type')),
                ('common_location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Common Location')),
            ],
            options={
                'verbose_name': 'Call',
                'verbose_name_plural': 'Calls',
            },
        ),
    ]
