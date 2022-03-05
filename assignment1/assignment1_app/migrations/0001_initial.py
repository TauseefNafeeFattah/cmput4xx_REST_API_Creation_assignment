# Generated by Django 4.0.1 on 2022-02-11 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeRoaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('farm', models.CharField(max_length=256)),
                ('region', models.CharField(max_length=256)),
                ('fermentation', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]