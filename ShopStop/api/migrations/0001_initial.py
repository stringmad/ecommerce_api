# Generated by Django 3.2.9 on 2022-01-30 17:39

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='PricingRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minprice', models.FloatField(db_index=True, max_length=150)),
                ('maxprice', models.FloatField(db_index=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('license', models.CharField(db_index=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Parent', to='api.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('price', models.FloatField(db_index=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=350, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile_pic', models.ImageField(blank=True, default='default.jpg', upload_to=api.models.user_directory_path)),
                ('region', models.CharField(choices=[('EU', 'Europe Region'), ('US', 'America Region'), ('China', 'China Region'), ('ROW', 'Rest of the World')], db_index=True, max_length=100)),
                ('Vendor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vendor_names', to='api.vendor')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produits', to='api.category')),
                ('price_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rangebetween', to='api.pricingrange')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produits', to='api.subcategory')),
            ],
        ),
    ]
