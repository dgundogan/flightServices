# Generated by Django 2.1.15 on 2020-03-19 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flightNumber', models.CharField(max_length=10)),
                ('operatingAirlines', models.CharField(max_length=20)),
                ('departureCity', models.CharField(max_length=20)),
                ('arrivalCity', models.CharField(max_length=20)),
                ('dateOfDeparture', models.DateField()),
                ('estimatedTimeOfDeparture', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firtname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('middleName', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flightApp.Flight')),
                ('passenger', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flightApp.Passenger')),
            ],
        ),
    ]
