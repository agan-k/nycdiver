# Generated by Django 4.2.4 on 2024-04-10 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='cta',
            field=models.CharField(blank=True, max_length=200, verbose_name='notes:'),
        ),
    ]
