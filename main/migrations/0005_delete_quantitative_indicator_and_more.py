# Generated by Django 5.1.7 on 2025-04-06 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_indicator_quantitative_indicator1_indicator1_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Quantitative_indicator',
        ),
        migrations.DeleteModel(
            name='Quantitative_indicator1',
        ),
    ]
