# Generated by Django 3.1.2 on 2020-11-04 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0004_auto_20201103_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sportlist',
            name='sports',
        ),
        migrations.DeleteModel(
            name='Sport',
        ),
        migrations.DeleteModel(
            name='Sportlist',
        ),
    ]
