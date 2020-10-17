# Generated by Django 3.1.2 on 2020-10-16 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20201016_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='nature',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='pstatus',
            field=models.CharField(blank=True, choices=[('Employed', 'Employed'), ('self-employed', 'self-employed')], default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='seva_area',
            field=models.CharField(blank=True, choices=[('Near_Home', 'Near_Home'), ('Near_Campus', 'Near_Home')], default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='seva_residential_pincode',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
