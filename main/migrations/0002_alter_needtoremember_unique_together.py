# Generated by Django 4.0.4 on 2022-10-01 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='needtoremember',
            unique_together={('card',)},
        ),
    ]
