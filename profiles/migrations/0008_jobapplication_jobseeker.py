# Generated by Django 5.0.7 on 2024-07-31 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_job_category_jobseeker_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='jobseeker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.jobseeker'),
        ),
    ]
