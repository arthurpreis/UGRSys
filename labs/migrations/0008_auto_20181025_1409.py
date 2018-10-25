# Generated by Django 2.1.2 on 2018-10-25 17:09

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0007_auto_20181021_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='waste',
            name='acetonitrile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='waste',
            name='amine',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='waste',
            name='cyanide',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='waste',
            name='halogen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='waste',
            name='heavy_metals',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='waste',
            name='pH',
            field=models.DecimalField(blank=True, decimal_places=0, default=Decimal('7'), max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name='waste',
            name='sulfur',
            field=models.BooleanField(default=False),
        ),
    ]