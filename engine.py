from stockfish import Stockfish
import chess
import pandas as pd
import numpy as np

stockfish = Stockfish(path="/Users/Jhon/stockfish/stockfish-windows-x86-64-avx2")
df = pd.read_csv("upset_dataset.csv")

# Examples of what stockfish can do
stockfish.set_position(["e2e4", "c7c5"])
stockfish.make_moves_from_current_position(["g1f3"])
# stockfish.set_fen_position("rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2")
print(stockfish.get_fen_position())
stockfish.get_best_move(wtime=1000, btime=1000)
print(stockfish.get_top_moves(3))

# Positive is advantage white, negative is advantage black
print(stockfish.get_evaluation())

# Example on how to convert secific FEN moves to coordinate
fen = "rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2"
board = chess.Board(fen)
algmove = 'Nf3'
coordmove = str(board.parse_san(algmove))
print(coordmove)


def set_moves(move_list):
    print(move_list)
    move_list = move_list.split()
    return move_list


class FishEngine:
    def __int__(self):
        self.num = 0
        self.moves = None
        self.board = chess.Board()
        self.fen = None

    def __int__(self, match):
        self.num = 0
        self.moves = set_moves(match)
        self.board = chess.Board()
        self.fen = None

    def resetBoard(self):
        self.board = chess.Board()

    def getFEN(self, move_list):
        for move in move_list:
            board.push_san(move)
        self.fen = board.fen()


#
df_moves = df["moves"]

test_moves = set_moves(df_moves[0])
board = chess.Board()
for i in range(8):
    board.push_san(test_moves[i])

print(board.fen())
