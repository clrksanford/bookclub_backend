# Generated by Django 2.2.6 on 2019-11-12 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191112_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='attendees', to='api.Event'),
        ),
    ]
