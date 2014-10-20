from rest_framework import serializers
from chessdb.models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game