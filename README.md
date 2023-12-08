# chess
Local chess game with full ruleset, made in Pygame.

# stockfish
Within the python file "engine.py", Stockfish must be downloaded from their website [Stockfish](https://stockfishchess.org/download/)

For window users go [here](https://stockfishchess.org/download/windows/) and download the 64-bit

Any additional information on using stockfish in python: [stockfish py](https://pypi.org/project/stockfish/)

# controls:
SPACE: flip board

R: reset/new game

A: auto-flip board after each turn

1-4: change promotion (1 = Queen, 2 = Knight, 3 = Rook, 4 = Bishop)

P: print game transcript to terminal

# files:
FreeSerif-4aeK.ttf: font file that is used for text and the unicode images of the chess pieces.

chess_piece_king.png: window icon image

main.py: main execution file

pieces.py: class file for the pieces

# notes:
Special credit to: 
(Note: As of 11/15/23, currently have yet to find the initial creator for the chessboard created using pygame)

## Below are notes given from creator "_____"
Functioning as of 23/01/21 but not fully bug tested/more features coming. Please send any feedback: basileagle@gmail.com

24/01/21: Fixed a MAJOR bug with 2 words. Line 30 of pieces.py should have read "COORDS not IN legal_moves", not "not legal_moves". Corrected in newest upload.
