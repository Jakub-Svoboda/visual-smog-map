# Generated by Django 4.2.3 on 2023-07-10 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Smog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('note', models.CharField(max_length=3000)),
                ('parcel', models.CharField(max_length=300)),
                ('lv', models.CharField(max_length=300)),
                ('legality_status', models.CharField(max_length=300)),
                ('latitude', models.CharField(max_length=300)),
                ('longitude', models.CharField(max_length=300)),
                ('cadaster', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]