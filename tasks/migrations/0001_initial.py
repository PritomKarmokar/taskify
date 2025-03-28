# Generated by Django 5.1.7 on 2025-03-27 20:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(default='initiated')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
