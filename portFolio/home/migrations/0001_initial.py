# Generated by Django 4.1.5 on 2023-01-16 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myBackGround',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TAS', models.CharField(max_length=50)),
                ('tas_eno', models.IntegerField()),
                ('tas_sal', models.FloatField()),
                ('tas_res', models.CharField(max_length=250)),
            ],
        ),
    ]
