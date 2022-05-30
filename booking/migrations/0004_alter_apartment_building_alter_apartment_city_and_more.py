# Generated by Django 4.0.4 on 2022-05-30 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_apartment_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='building',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='conditioner',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='kitchen',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='medicine',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='tv',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='type',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='washmash',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='wifi',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]