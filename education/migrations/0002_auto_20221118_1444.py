# Generated by Django 3.2 on 2022-11-18 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='board',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='registration_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='roll_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]