from stockfish import Stockfish

stockfish = Stockfish(path="/Users/Jhon/stockfish/stockfish-windows-x86-64")

stockfish.set_position(["e2e4", "e7e5"])
stockfish.make_moves_from_current_position(["g1f3", "b8c6", "f1c4"])
stockfish.get_best_move(wtime=1000, btime=1000)


print(stockfish.get_top_moves(3))

# Positive is advantage white, negative is advantage black
print(stockfish.get_evaluation())

