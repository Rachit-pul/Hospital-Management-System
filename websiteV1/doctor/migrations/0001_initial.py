# Generated by Django 3.0.4 on 2020-03-07 15:23

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=100)),
            ],
            managers=[
                ('value', django.db.models.manager.Manager()),
            ],
        ),
    ]
