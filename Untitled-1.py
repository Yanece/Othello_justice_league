

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

