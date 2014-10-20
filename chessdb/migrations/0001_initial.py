# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('game_date', models.DateTimeField(blank=True)),
                ('event_date', models.DateTimeField(blank=True)),
                ('pgn', models.TextField()),
                ('white_player', models.CharField(max_length=100, blank=True)),
                ('black_player', models.CharField(max_length=100, blank=True)),
                ('event', models.CharField(max_length=100, blank=True)),
                ('site', models.CharField(max_length=100, blank=True)),
                ('result', models.CharField(max_length=10, blank=True)),
                ('white_title', models.CharField(max_length=10, blank=True)),
                ('black_title', models.CharField(max_length=10, blank=True)),
                ('white_elo', models.FloatField(blank=True)),
                ('black_elo', models.FloatField(blank=True)),
                ('eco', models.CharField(max_length=10, blank=True)),
                ('opening', models.CharField(max_length=100, blank=True)),
                ('variation', models.CharField(max_length=100, blank=True)),
                ('white_fide_id', models.CharField(max_length=15, blank=True)),
                ('black_fide_id', models.CharField(max_length=15, blank=True)),
            ],
            options={
                'ordering': ('game_date',),
            },
            bases=(models.Model,),
        ),
    ]
