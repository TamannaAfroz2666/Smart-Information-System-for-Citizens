# Generated by Django 3.2 on 2022-11-14 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passport', '0002_auto_20221111_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='passport',
            name='is_verify',
            field=models.BooleanField(default=False),
        ),
    ]