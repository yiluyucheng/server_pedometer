# Generated by Django 4.0.5 on 2022-07-14 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('step', '0003_session_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='end',
            field=models.CharField(default=0, max_length=30, verbose_name='End'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='start',
            field=models.CharField(default=0, max_length=30, verbose_name='Start'),
            preserve_default=False,
        ),
    ]