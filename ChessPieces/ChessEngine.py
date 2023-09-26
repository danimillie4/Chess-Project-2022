# STORES DATA FOR THE GAME STATE
# DETERMINES VALID CHESS MOVES
# KEEPS A MOVE LOG

class GameState():
    def __init__(self):
        # GAME_BOARD IS AN 8X8 2 DIMENSIONAL ARRAY WHICH REPRESENTS THE CHESS BOARD
        # ELEMENTS BEGINNING WITH A 'B' OR 'W' REPRESENTS WHETHER THE ELEMENT IS A BLACK OR WHITE PIECE
        # THE SECOND LETTER REPRESENTS THE CHESS PIECE (FOR EXAMPLE, 'K' MEANS KING)
        # '__' MEANS THE SQUARE IS BLANK
        self.board = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                      ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                      ["__", "__", "__", "__", "__", "__", "__", "__"],
                      ["__", "__", "__", "__", "__", "__", "__", "__"],
                      ["__", "__", "__", "__", "__", "__", "__", "__"],
                      ["__", "__", "__", "__", "__", "__", "__", "__"],
                      ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                      ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        #  self.move_functions = {"P": self.pawn_moves, "R": self.rook_moves, "B": self.bishop_moves,
        #  "N": self.knight_moves, "Q": self.queen_moves, "K": self.king_moves, }
        self.white_move = True
        self.move_log = []

    def make_move(self, move):
        # TAKES A MOVE IN AS A PARAMETER AND EXECUTES IT
        # ^NOT FOR CASTLING, PAWN PROMOTION AND EN PASSANT
        # ALLOWS PLAYERS TO MAKE THEIR MOVES
        self.board[move.st_row][move.st_column] = "__"
        self.board[move.end_row][move.end_column] = move.moves_piece
        self.move_log.append(move)  # LOGS MOVE SO THAT IT CAN BE UNDONE LATER
        self.white_move = not self.white_move  # SWAP PLAYERS TURNS

    def undo_move(self):
        # THIS WILL UNDO THE LAST MOVE MADE
        if len(self.move_log) != 0:  # ENSURING HAT THERE'S A MOVE TO UNDO
            move = self.move_log.pop()
            self.board[move.st_row][move.st_column] = move.moves_piece
            self.board[move.end_row][move.end_column] = move.captured_piece
            self.white_move = not self.white_move  # SWITCHES TURN BACK

    def get_valid_move(self):
        # CONSIDERS CHECKS WHEN MOVES ARE MADE
        return self.get_possible_moves()

    def get_possible_moves(self):
        # DOESN'T CONSIDER CHECKS WHEN MOVES ARE MADE
        moves = []
        for row in range(len(self.board)):  # NUM OF ROWS
            for column in range(len(self.board[row])):  # NUM FOR COLUMNS IN GIVEN ROWS
                turn = self.board[row][column][0]
                if (turn == "w" and self.white_move) or (turn == "b" and not self.white_move):
                    piece = self.board[row][column][1]
                    if piece == "P":
                        self.pawn_moves(row, column, moves)
                    elif piece == "R":
                        self.rook_moves(row, column, moves)
                    elif piece == "B":
                        self.bishop_moves(row, column, moves)
                    elif piece == "N":
                        self.knight_moves(row, column, moves)
                    elif piece == "Q":
                        self.queen_moves(row, column, moves)
                    elif piece == "K":
                        self.king_moves(row, column, moves)
        return moves

    def pawn_moves(self, row, column, moves):
        # GET ALL PAWN MOVES AND ADD THEM TO THE LIST
        if self.white_move:  # IF THE WHITE PAWN MOVES
            if self.board[row-1][column] == "__":  # PAWN MOVING AHEAD BY 1 SQUARE
                moves.append(Moves((row, column), (row-1, column), self.board))
                if row == 6 and self.board[row-2][column] == "__":  # PAWN MOVING AHEAD BY 2 SQUARES
                    moves.append(Moves((row, column), (row-2, column), self.board))
            if column-1 >= 0:  # CAPTURES TO THE LEFT
                if self.board[row-1][column-1][0] == "b":  # WHITE CAN CAPTURE THE BLACK PIECE
                    moves.append(Moves((row, column), (row-1, column-1), self.board))
            if column+1 <= 7:  # CAPTURES TO THE RIGHT
                if self.board[row-1][column+1][0] == "b":
                    moves.append(Moves((row, column), (row-1, column+1), self.board))

        elif not self.white_move:  # IF ITS BLACKS TURN TO MOVE
            if self.board[row+1][column] == "__":  # BLACK PAWN MOVING AHEAD BY 1
                moves.append(Moves((row, column), (row+1, column), self.board))
                if row == 1 and self.board[row+2][column] == "__":  # BLACK PAWN MOVING AHEAD BY 2 SQUARES
                    moves.append(Moves((row, column), (row+2, column), self.board))
            if column-1 >= 0:  # CAPTURES TO BLACKS RIGHT
                if self.board[row+1][column-1][0] == "w":  # BLACK PIECE CAN CAPTURE WHITE PIECE
                    moves.append(Moves((row, column), (row+1, column-1), self.board))
            if column+1 <= 7:  # CAPTURES TO BLACKS LEFT
                if self.board[row+1][column+1][0] == "w":
                    moves.append(Moves((row, column), (row+1, column+1), self.board))

    def rook_moves(self, row, column, moves):
        # GET ALL ROOK MOVES AND ADD THEM TO THE LIST
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))  # UP, DOWN, LEFT RIGHT (ROOK MOVES)
        if self.white_move:  # ENSURING THAT OPPOSITE TEAMS CAN CAPTURE EACH OTHER
            enemy = "b"
        else:
            enemy = "w"
        for d in directions:  # USING THE MOVES FROM THE DIRECTIONS TUPLE
            for i in range(1, 8):  # ENSURING THAT THE PIECES STAY IN THE TABLE
                end_row = row + d[0] * i
                end_column = column + d[1] * i
                if 0 <= end_row < 8 and 0 <= end_column < 8:
                    end_piece = self.board[end_row][end_column]
                    if end_piece == "__":  # ROOK MOVING TO AN EMPTY SPACE
                        moves.append(Moves((row, column), (end_row, end_column), self.board))
                    elif end_piece[0] == enemy:  # ROOK CAPTURING ENEMY
                        moves.append(Moves((row, column), (end_row, end_column), self.board))
                        break
                    else:  # CAN'T CAPTURE ITS OWN PIECE
                        break
                else:  # IF THE PIECE ISN'T IN RANGE IT CANT MOVE
                    break

    def bishop_moves(self, row, column, moves):
        # GET ALL BISHOP MOVES AND ADD THEM TO THE LIST
        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))  # BISHOP MOVES
        enemy = "b" if self.white_move else "w"  # ENSURING THAT THE OPPOSITE TEAMS CAN CAPTURE EACH OTHER
        for d in directions:  # USING THE MOVES FROM THE DIRECTIONS TUPLE
            for i in range(1, 8):  # ENSURING THAT THE PIECES STAY IN THE TABLE
                end_row = row + d[0] * i
                end_column = column + d[1] * i
                if 0 <= end_row < 8 and 0 <= end_column < 8:
                    end_piece = self.board[end_row][end_column]
                    if end_piece == "__":  # BISHOP MOVES TO AN EMPTY SPACE
                        moves.append(Moves((row, column), (end_row, end_column), self.board))
                    elif end_piece[0] == enemy:  # BISHOP CAPTURES OPPONENT
                        moves.append(Moves((row, column), (end_row, end_column), self.board))
                        break
                    else:  # PLAYERS CAN'T CAPTURE ITS OWN PIECE
                        break
                else:  # IF THE PIECE ISN'T IN RANGE IT CAN'T MOVE
                    break

    def knight_moves(self, row, column, moves):
        # GET ALL KNIGHT MOVES AND ADD THEM TO THE LIST
        directions = ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2))  # KNIGHT MOVES
        enemy = "b" if self.white_move else "w"  # ENSURING THAT THE OPPOSITE TEAMS CAN CAPTURE EACH OTHER
        for d in directions:  # USING THE MOVES FROM THE DIRECTIONS TUPLE
            for i in range(1, 8):  # ENSURING THAT THE PIECES STAY IN THE TABLE
                end_row = row + d[0] * i
                end_column = column + d[1] * i
                if 0 <= end_row < 8 and 0 <= end_column < 8:
                    end_piece = self.board[end_row][end_column]
                    if end_piece == "__":  # KNIGHT MOVES TO AN EMPTY SPACE
                        moves.append(Moves((row, column), (end_row, end_column), self.board))
                    elif end_piece[0] == enemy:  # KNIGHT CAPTURES OPPONENT
                        moves.append(Moves((row, column), (end_row, end_column), self.board))
                        break
                    else:  # PLAYERS CAN'T CAPTURE ITS OWN PIECE
                        break
                else:  # IF THE PIECE ISN'T IN RANGE IT CAN'T MOVE
                    break

    def queen_moves(self, row, column, moves):
        # GET ALL QUEEN MOVES AND ADD THEM TO THE LIST
        # CALLS TO THE ROOK MOVES METHOD AS THE QUEEN MOVES IN THE SAME WAY AS THE ROOK...
        # BUT ALSO MOVES IN THE SAME WAY AS THE BISHOP SO I CAN CALL BOTH THE FUNCTIONS HERE TO OPERATE THE QUEEN
        self.rook_moves(row, column, moves)
        self.bishop_moves(row, column, moves)

    def king_moves(self, row, column, moves):
        # GET ALL KING MOVES AND ADD THEM TO THE LIST
        directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))  # TUPLE OF ALL KING MOVES
        ally = "w" if self.white_move else "b"  # DEFINING WHO'S THE ENEMY
        for i in range(8):  # ENSURING THAT THE PIECES ARE ON THE BOARD AND STAY ON THE BOARD AS THEY MOVE
            end_row = row + directions[i][0]
            end_column = column + directions[i][1]
            if 0 <= end_row < 8 and 0 <= end_column < 8:
                end_piece = self.board[end_row][end_column]
                if end_piece[0] != ally:  # ALLOWING THE KING TO CAPTURE ENEMY PIECES
                    moves.append(Moves((row, column), (end_row, end_column), self.board))


class Moves():
    # USING DICTIONARIES THIS MAPS KEYS TO THEIR VALUES
    # KEY: VALUE
    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4,
                     "5": 3, "6": 2, "7": 1, "8": 0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_columns = {"a": 0, "b": 1, "c": 2, "d": 3,
                        "e": 4, "f": 5, "g": 6, "h": 7}
    columns_to_files = {v: k for k, v in files_to_columns.items()}

    # STORES ALL THE INFORMATION ABOUT A MOVE
    def __init__(self, st_square, end_square, board):
        self.st_row = st_square[0]
        self.st_column = st_square[1]
        self.end_row = end_square[0]
        self.end_column = end_square[1]
        self.moves_piece = board[self.st_row][self.st_column]
        self.captured_piece = board[self.end_row][self.end_column]
        self.move_id = self.st_row * 1000 + self.st_column * 100 + self.end_row * 10 + self.end_column

    def __eq__(self, other):
        if isinstance(other, Moves):
            return self.move_id == other.move_id
        return False

# ALLOWS US TO SEE MOVES IN CHESS NOTATION
    def get_chess_notation(self):
        return self.get_rank_file(self.st_row, self.st_column) + self.get_rank_file(self.end_row, self.end_column)

    def get_rank_file(self, rank, column):
        # HELPER METHOD FOR GET_CHESS_NOTATION
        return self.columns_to_files[column] + self.rows_to_ranks[rank]

