# Generated by Django 5.0.6 on 2024-09-02 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grocery_app', '0005_stockx_stock_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockx',
            name='stock_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
