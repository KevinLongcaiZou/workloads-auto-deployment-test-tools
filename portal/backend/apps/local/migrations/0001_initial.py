# Generated by Django 3.1.1 on 2022-03-23 03:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocalInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('password', models.CharField(blank=True, max_length=30, null=True)),
                ('ip', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, default=list, null=True, size=None)),
                ('region', models.CharField(blank=True, max_length=30, null=True)),
                ('instance_type', models.CharField(blank=True, max_length=30, null=True)),
                ('cpu_arch', models.CharField(blank=True, max_length=30, null=True)),
                ('cpu_model', models.CharField(blank=True, max_length=255, null=True)),
                ('memory_num', models.CharField(blank=True, max_length=30, null=True)),
                ('memory_size', models.CharField(blank=True, max_length=30, null=True)),
                ('disk', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, default=list, null=True, size=None)),
                ('user', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.CharField(blank=True, choices=[('CREATED', 'CREATED'), ('CREATING', 'CREATING'), ('DELETED', 'DELETED'), ('DELETING', 'DELETING'), ('NOT_START', 'NOT_START'), ('FAILED', 'FAILED'), ('CREATE_FAILED', 'CREATE_FAILED'), ('DELETE_FAILED', 'DELETE_FAILED')], default='CREATED', max_length=30, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='LocalJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workload', models.CharField(blank=True, max_length=128, null=True)),
                ('config', models.CharField(blank=True, max_length=128, null=True)),
                ('machines', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, default=list, null=True, size=None)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('fail_reason', models.CharField(blank=True, max_length=512, null=True)),
                ('provision_id', models.CharField(blank=True, max_length=10, null=True)),
                ('status', models.CharField(blank=True, choices=[('NOT_START', 'NOT_START'), ('RUNNING', 'RUNNING'), ('FAILED', 'FAILED'), ('FINISHED', 'FINISHED')], default='NOT_START', max_length=30, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]