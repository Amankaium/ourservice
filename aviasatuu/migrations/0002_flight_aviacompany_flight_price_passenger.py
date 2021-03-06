# Generated by Django 4.0.4 on 2022-05-25 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aviasatuu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='aviacompany',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('document', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('date_birth', models.CharField(max_length=255)),
                ('document_number', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
