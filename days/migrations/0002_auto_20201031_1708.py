# Generated by Django 3.1.2 on 2020-10-31 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('days', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='events',
        ),
        migrations.AddField(
            model_name='day',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='eventsofday', to='days.Events'),
        ),
        migrations.RemoveField(
            model_name='days',
            name='day',
        ),
        migrations.AddField(
            model_name='days',
            name='day',
            field=models.ManyToManyField(blank=True, related_name='dayofdays', to='days.Day'),
        ),
    ]