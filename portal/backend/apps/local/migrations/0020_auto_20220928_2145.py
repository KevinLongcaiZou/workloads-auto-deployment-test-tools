# Generated by Django 3.2.15 on 2022-09-28 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0019_alter_localjob_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='localjob',
            name='filter_case',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='localjob',
            name='result_link',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]