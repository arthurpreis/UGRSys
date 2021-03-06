# Generated by Django 2.1.2 on 2018-10-21 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0006_auto_20181021_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waste',
            name='can_agitate',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('NÃO SEI', 'Não Sei')], default='SIM', max_length=7),
        ),
        migrations.AlterField(
            model_name='waste',
            name='corrosive',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('NÃO SEI', 'Não Sei')], default='SIM', max_length=7),
        ),
        migrations.AlterField(
            model_name='waste',
            name='explosive',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('NÃO SEI', 'Não Sei')], default='SIM', max_length=7),
        ),
        migrations.AlterField(
            model_name='waste',
            name='flammable',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('NÃO SEI', 'Não Sei')], default='SIM', max_length=7),
        ),
        migrations.AlterField(
            model_name='waste',
            name='health_dangerous',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('NÃO SEI', 'Não Sei')], default='SIM', max_length=7),
        ),
        migrations.AlterField(
            model_name='waste',
            name='oxidizing',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('NÃO SEI', 'Não Sei')], default='SIM', max_length=7),
        ),
        migrations.AlterField(
            model_name='waste',
            name='pollutant',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('NÃO SEI', 'Não Sei')], default='SIM', max_length=7),
        ),
        migrations.AlterField(
            model_name='waste',
            name='toxic',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('NÃO SEI', 'Não Sei')], default='SIM', max_length=7),
        ),
        migrations.AlterField(
            model_name='waste',
            name='under_pressure',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('NÃO SEI', 'Não Sei')], default='SIM', max_length=7),
        ),
    ]
