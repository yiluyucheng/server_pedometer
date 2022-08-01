# Generated by Django 4.0.5 on 2022-08-01 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('step', '0005_alter_session_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='age',
            field=models.FloatField(default=0, verbose_name='Age'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='height',
            field=models.IntegerField(default=0, verbose_name='Height'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='sex',
            field=models.CharField(default=0, max_length=10, verbose_name='Sex'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='weight',
            field=models.FloatField(default=0, verbose_name='Weight'),
            preserve_default=False,
        ),
    ]