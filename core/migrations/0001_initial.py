# Generated by Django 3.0.7 on 2020-11-11 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DirectionPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_from', models.CharField(max_length=10)),
                ('city_to', models.CharField(max_length=10)),
                ('price', models.PositiveIntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]