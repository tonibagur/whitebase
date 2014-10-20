# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chessdb', '0003_auto_20141018_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='event_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_date',
            field=models.DateField(null=True),
        ),
    ]
