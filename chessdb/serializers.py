from rest_framework import serializers
from chessdb.models import Game
import chess.pgn
from StringIO import StringIO

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
    moves=serializers.SerializerMethodField('get_moves')
    def get_moves(self,obj):
        s=StringIO()
        s.write(obj.pgn)
        s.seek(0)
        node=chess.pgn.read_game(s)
        moves=[{'move':'initial',
                'fen':node.board().fen()}]
        while node.variations:
            next_node=node.variations[0]
            moves.append({'move':node.board().san(next_node.move),
                          'fen':next_node.board().fen()})
            node=next_node
        return moves
