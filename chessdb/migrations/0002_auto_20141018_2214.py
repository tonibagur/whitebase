# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chessdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_date',
            field=models.DateTimeField(null=True),
        ),
    ]
