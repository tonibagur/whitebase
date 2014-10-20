# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chessdb', '0002_auto_20141018_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='black_elo',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='black_fide_id',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='black_player',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='black_title',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='eco',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='event',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='event_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='opening',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='result',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='site',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='variation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='white_elo',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='white_fide_id',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='white_player',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='white_title',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
