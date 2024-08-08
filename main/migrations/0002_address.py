# Generated by Django 5.0.7 on 2024-08-08 15:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('address1', models.CharField(max_length=60, verbose_name='Address line 1')),
                ('address2', models.CharField(blank=True, max_length=60, verbose_name='Address line 2')),
                ('zip_code', models.CharField(max_length=12, verbose_name='ZIP / Postal code')),
                ('city', models.CharField(max_length=60)),
                ('country', models.CharField(choices=[('md', 'Moldova, Republic of'), ('ro', 'Romania'), ('ua', 'Ukraine'), ('uk', 'United Kingdom'), ('us', 'United States of America')], max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
