# Generated by Django 4.0.4 on 2022-05-30 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erkindik', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='art',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]