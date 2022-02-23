# Generated by Django 3.2 on 2022-02-18 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fresherjob', '0002_alter_fresherjob_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='jovvacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, verbose_name='Email Address')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Post Date')),
                ('company', models.CharField(max_length=500, verbose_name='Company Name')),
                ('location', models.CharField(max_length=500, verbose_name='Location')),
                ('role_name', models.CharField(max_length=500, verbose_name='Role Name')),
                ('job_experience', models.CharField(max_length=500, verbose_name='Job Experience')),
                ('qualifications', models.CharField(max_length=500, verbose_name='Qualifications')),
                ('application_link', models.URLField(blank=True, max_length=500, null=True, verbose_name='Reference link')),
            ],
            options={
                'verbose_name': 'Vacancie',
            },
        ),
    ]
