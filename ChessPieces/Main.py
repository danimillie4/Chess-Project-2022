# MAIN SECTION OF THE PROJECT RESPONSIBLE FOR USER INPUT AND
# CURRENT GAME STATE

import pygame as py
#from ChessPieces import Menu
from ChessPieces import ChessEngine


# DEFINING VARIABLES FOR THE FORMAT OF THE GAME
width = 672
height = 672
dimension = 8  # CHESS BOARD DIMENSIONS ARE 8X8
square_size = height // dimension
IMAGES = {}


# INITIALISING A GLOBAL DICTIONARY OF IMAGES
# FOR LOOP AND ARRAY ENSURES THAT IT WILL ONLY HAVE TO BE CALLED ONCE TO THE MAIN
def load_images():
    pieces = ["wR", "wN", "wB", "wQ", "wK", "wP", "bR", "bN", "bB", "bQ", "bK", "bP"]
    for piece in pieces:
        IMAGES[piece] = py.transform.scale(py.image.load("chess_Pieces/" + piece + ".png"),
                                           (square_size, square_size))
        # IMAGES['wP'] = p.image.load("images/wP.png") works but is less efficient
        # ACCESS AN IMAGE BY CALLING 'IMAGES['wP']'


# THE MAIN FOR THE CODE
# HANDLES USER INPUT
def main():
    py.init()
    screen = py.display.set_mode((width, height))
    screen.fill(py.Color("white"))
    gs = ChessEngine.GameState()
    valid_move = gs.get_valid_move()
    moves_made = False  # CHECK / FLAG VARIABLE FOR WHEN A MOVE IS MADE
    load_images()  # CALLING IMAGES ONCE BEFORE WHILE LOOP
    running = True
    square_selected = ()  # NONE OF THE SQUARES ARE SELECTED YET, IT KEEPS TRACK OF THE USERS LAST CLICK(TUPLE)
    user_clicks = []  # KEEPS TRACK OF THE USERS CLICKS (2 TUPLES)

    while running:
        for i in py.event.get():
            if i.type == py.quit:
                running = False
            # MOUSE HANDLER
            elif i.type == py.MOUSEBUTTONDOWN:
                location = py.mouse.get_pos()  # COORDINATES OF THE MOUSE
                column = location[0]//square_size
                row = location[1]//square_size
                if gs.board[row][column] == '__' and len(user_clicks) == 0:
                    continue
                if square_selected == (row, column):  # IF THE USER CLICKS THE SAME SQUARE TWICE
                    square_selected = ()  # DESELECTS
                    user_clicks = []  # CLEARS PLAYER CLICKS
                else:
                    square_selected = (row, column)
                    user_clicks.append(square_selected)  # APPEND FOR FIRST AND SECOND CLICKS
                if len(user_clicks) == 2:  # MEANING ITS AFTER THE SECOND CLICK
                    move = ChessEngine.Moves(user_clicks[0], user_clicks[1], gs.board)
                    print(move.get_chess_notation())
                    if move in valid_move:
                        gs.make_move(move)
                        moves_made = True
                        square_selected = ()  # THIS RESETS THE USER CLICKS
                        user_clicks = []
                    else:
                        user_clicks = [square_selected]
            # KEY HANDLERS
            elif i.type == py.KEYDOWN:
                if i.key == py.K_b:  # UNDO MOVE WHEN "b" IS PRESSED
                    gs.undo_move()
                    moves_made = True
        if moves_made:
            valid_move = gs.get_valid_move()
            moves_made = False

        draw_game_state(screen, gs)
        py.display.flip()
        draw_game_state(screen, gs)


# RESPONSIBLE FO GRAPHICS WITHIN THE CURRENT GAME STATE
def draw_game_state(screen, gs):
    draw_board(screen)  # THIS DRAWS SQUARES TO THE BOARD
    draw_pieces(screen, gs.board)  # THIS DRAWS THE PIECES ON TOP OF THE SQUARES ON THE BOARD


# DRAWS SQUARES TO THE BOARD
def draw_board(screen):
    colors = [py.Color(105, 127, 140), py.Color(191, 191, 191)]
    for row in range(dimension):
        for column in range(dimension):
            colour = colors[((row+column) % 2)]
            py.draw.rect(screen, colour, py.Rect(column*square_size, row*square_size, square_size, square_size))


# DRAWS PIECES TO THE BOAR CALLED IN draw_game_state
def draw_pieces(screen, board):
    for row in range(dimension):
        for column in range(dimension):
            piece = board[row][column]
            if piece != "__":   # IF ITS NOT AN EMPTY SQUARE
                screen.blit(IMAGES[piece], py.Rect(column*square_size, row*square_size, square_size, square_size))


if __name__ == "__main__":
    main()
