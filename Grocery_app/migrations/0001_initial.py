# Generated by Django 5.0.6 on 2024-08-13 20:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stockx',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=50, null=True)),
                ('stock_type', models.CharField(blank=True, max_length=50, null=True)),
                ('stock_source', models.CharField(blank=True, max_length=50, null=True)),
                ('unit_cost', models.IntegerField(blank=True, default=0, null=True)),
                ('unit_price', models.IntegerField(blank=True, default=0, null=True)),
                ('total_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('stock_branch', models.CharField(blank=True, max_length=50, null=True)),
                ('issued_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('stock_contact', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('amount_received', models.IntegerField(blank=True, default=0, null=True)),
                ('issued_to', models.CharField(blank=True, max_length=50, null=True)),
                ('unit_price', models.IntegerField(blank=True, default=0, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grocery_app.stockx')),
            ],
        ),
    ]