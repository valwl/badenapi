# Generated by Django 5.0.1 on 2024-01-31 16:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('guest', models.PositiveIntegerField()),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('weekend_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='media/img/baden_samer.jpeg')),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='img/apartment/vogue11jpeg', upload_to='img/apartment')),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.apartment')),
            ],
        ),
        migrations.AddField(
            model_name='apartment',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.category'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.location'),
        ),
        migrations.CreateModel(
            name='LocationImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='img/apartment/bali_hotel_livingroom.jpeg', upload_to='img/apartment')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.location')),
            ],
        ),
    ]
