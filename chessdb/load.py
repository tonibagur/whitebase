from chessdb.models import Game
import chess.pgn
import datetime

def load_pgn_file(file_name):
    pgn=open(file_name,'r')
    game_read=True
    while game_read:
        game_read=chess.pgn.read_game(pgn)
        if game_read:
            game_db=Game()
            date_parts=map(int,game_read.headers['Date'].split('.'))
            game_db.game_date = datetime.date(date_parts[0],date_parts[1],date_parts[2])
            date_parts=map(int,game_read.headers['EventDate'].split('.'))
            game_db.event_date = datetime.date(date_parts[0],date_parts[1],date_parts[2])
            game_db.pgn = str(game_read) + '\n\n'
            game_db.white_player = game_read.headers['White']
            game_db.black_player = game_read.headers['Black']
            game_db.event = game_read.headers['Event']
            game_db.site = game_read.headers['Site']
            game_db.result = game_read.headers['Result']
            try:
                game_db.white_title = game_read.headers['WhiteTitle']
            except:
                pass
            try:
                game_db.black_title = game_read.headers['BlackTitle']
            except:
                pass
            try:
                game_db.white_elo = game_read.headers['WhiteElo']
            except:
                pass
            try:
                game_db.black_elo = game_read.headers['BlackElo']
            except:
                pass
            try:
                game_db.eco = game_read.headers['ECO']
            except:
                pass
            try:
                game_db.opening = game_read.headers['Opening']
            except:
                pass
            try:
                game_db.variation = game_read.headers['Variation']
            except:
                pass
            try:
                game_db.white_fide_id = game_read.headers['WhiteFideId']
            except:
                pass
            try:
                game_db.black_fide_id = game_read.headers['BlackFideId']
            except:
                pass
            game_db.save()