# Generated by Django 3.1.2 on 2020-11-02 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('image', models.CharField(max_length=1000)),
                ('registration', models.TextField(blank=True)),
                ('howtoplay', models.TextField(blank=True)),
                ('sporthead', models.CharField(max_length=64)),
                ('fees', models.IntegerField(max_length=10)),
                ('door', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Sportlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageOne', models.CharField(max_length=1000)),
                ('imageTwo', models.CharField(max_length=1000)),
                ('quoteOne', models.CharField(max_length=200)),
                ('quoteTwo', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('sports', models.ManyToManyField(blank=True, related_name='sportsofsportlist', to='sports.Sport')),
            ],
        ),
    ]