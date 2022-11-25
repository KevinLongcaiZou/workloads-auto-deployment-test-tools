# Generated by Django 3.1.1 on 2022-04-26 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0012_localinstance_hostname'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalInstanceJobQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance_id', models.PositiveIntegerField(max_length=50)),
                ('job_id', models.PositiveIntegerField(max_length=50)),
                ('status', models.CharField(blank=True, choices=[('IN_QUEUE', 'IN_QUEUE'), ('RUNNING', 'RUNNING'), ('FINISHED', 'FINISHED')], default='IN_QUEUE', max_length=30, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='localjob',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='localjob',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]