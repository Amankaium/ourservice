# Generated by Django 4.0.4 on 2022-05-30 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apartment',
            old_name='coutry',
            new_name='country',
        ),
        migrations.AddField(
            model_name='apartment',
            name='bath',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='apartment',
            name='bed',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='apartment',
            name='building',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='apartment',
            name='conditioner',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='apartment',
            name='flat',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='guest',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='apartment',
            name='kitchen',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='apartment',
            name='medicine',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='apartment',
            name='room',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='apartment',
            name='tv',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='apartment',
            name='type',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='apartment',
            name='washmash',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='apartment',
            name='wifi',
            field=models.CharField(default='', max_length=255),
        ),
    ]
