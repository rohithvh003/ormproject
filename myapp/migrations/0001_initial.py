# Generated by Django 5.1.3 on 2024-12-05 05:30

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
                ('Sid', models.IntegerField()),
                ('Sname', models.CharField(max_length=30)),
                ('Smarks', models.FloatField()),
                ('Sage', models.IntegerField()),
                ('Sgender', models.IntegerField()),
                ('Splace', models.CharField(max_length=30)),
            ],
        ),
    ]
