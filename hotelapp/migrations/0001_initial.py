# Generated by Django 5.0.2 on 2024-10-20 20:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=255)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('base_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('customer_name', models.CharField(max_length=255)),
                ('total_price', models.IntegerField()),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotelapp.room')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotelapp.roomcategory'),
        ),
        migrations.CreateModel(
            name='SpecialRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('rate_multiplier', models.IntegerField()),
                ('room_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotelapp.roomcategory')),
            ],
        ),
    ]
