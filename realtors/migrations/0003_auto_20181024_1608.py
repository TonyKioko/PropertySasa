# Generated by Django 2.1.2 on 2018-10-24 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_auto_20181024_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
