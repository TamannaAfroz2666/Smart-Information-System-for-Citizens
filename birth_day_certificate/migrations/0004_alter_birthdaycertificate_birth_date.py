# Generated by Django 3.2 on 2022-11-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birth_day_certificate', '0003_auto_20221111_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthdaycertificate',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]