# Generated by Django 3.2 on 2022-02-19 19:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='updatedate',
            field=models.DateTimeField(auto_now=True, verbose_name='Update Date'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Post Date'),
        ),
    ]