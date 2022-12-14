# Generated by Django 4.1.3 on 2022-11-10 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
                ('contact', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('branch', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
