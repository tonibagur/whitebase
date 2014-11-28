from rest_framework import serializers
from chessdb.models import Game
import chess.pgn
import chess
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
                'fen':node.board().fen(),
                'tempo':-1}]
        i=0
        while node.variations:
            next_node=node.variations[0]
            moves.append({'move':node.board().san(next_node.move),
                          'fen':next_node.board().fen(),
                          'tempo':i,
                          'from':chess.SQUARE_NAMES[next_node.move.from_square],
                          'to':chess.SQUARE_NAMES[next_node.move.to_square],})
            node=next_node
            i+=1
        return moves
