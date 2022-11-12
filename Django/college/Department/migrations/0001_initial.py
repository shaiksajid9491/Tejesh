# Generated by Django 4.1.3 on 2022-11-12 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('age', models.IntegerField()),
                ('salary', models.FloatField()),
            ],
        ),
    ]
