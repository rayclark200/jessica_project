# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-23 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='login_app.User')),
            ],
        ),
    ]
