# Generated by Django 2.2.5 on 2020-01-09 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0009_auto_20200109_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DB.Address'),
        ),
    ]
