# Generated by Django 4.2.4 on 2024-04-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_alter_event_cover_charge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='cover_charge',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes'), ('N/A', 'N/A')], default=None, max_length=16, null=True, verbose_name='cover charge?'),
        ),
    ]
