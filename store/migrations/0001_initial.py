# Generated by Django 4.2.3 on 2023-08-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('descriptin', models.CharField(max_length=2000)),
                ('price', models.IntegerField()),
                ('image', models.CharField(max_length=2500)),
            ],
        ),
    ]
