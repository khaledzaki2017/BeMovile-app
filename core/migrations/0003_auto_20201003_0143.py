# Generated by Django 2.2 on 2020-10-02 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201002_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='wizardform',
            name='Razon_social',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='wizardform',
            name='home_address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='wizardform',
            name='nit',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='wizardform',
            name='question1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wizardform',
            name='question2',
            field=models.BooleanField(default=False),
        ),
    ]
