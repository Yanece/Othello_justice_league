

class Bot:
    def __init__(self, name):
        self.name = name

    # BOT FUNCTIONS
    def check_valid_moves(self, board, color):
        valid_moves = []
        max_pawns_flipped = 0
        best_move = []

        for tile in board.board:
            x_pos, y_pos = tile.x_pos, tile.y_pos

            if board.is_tile_empty(x_pos, y_pos):
                move_result = board.is_legal_move(x_pos, y_pos, color)
                if move_result:
                    # Calculer le score total pour ce mouvement
                    total_flipped = sum([result[0] for result in move_result])
                    if total_flipped > max_pawns_flipped:
                        max_pawns_flipped = total_flipped
                        best_move = [[x_pos, y_pos, total_flipped]]
                    elif total_flipped == max_pawns_flipped  :
                        best_move.append([[x_pos, y_pos, total_flipped]])
                    

        return random.choice(best_move)



def check_valid moves(self):
    new_board = Board(8)
    new_board.create_board()
    matrice_list = [100, -20, 10, 5, 5, 10, -20, 100,
        -20, -50, -2, -2, -2, -2, -50, -20,
        10, -2, 8, 1, 1, 8, -2, 10,
        5, -2, 1, 2, 2, 1, -2, 5,
        5, -2, 1, 2, 2, 1, -2, 5,
        10, -2, 8, 1, 1, 8, -2, 10,
        -20, -50, -2, -2, -2, -2, -50, -20,
        100, -20, 10, 5, 5, 10, -20, 100]
    for current_tile in range(new_board.board):
        new_board.board[current_tile].weight = matrice_list[current_tile]

