class Bot:
    # ...

    def check_valid_moves(self, board, color):
        # ... (le reste du code précédent)

        # Ajouter une vérification pour les coins pour augmenter leur priorité
        corner_positions = [(0, 0), (0, 7), (7, 0), (7, 7)]
        for move in valid_moves:
            x_pos, y_pos = move[0], move[1]
            if (x_pos, y_pos) in corner_positions:
                move.append(1000)  # Ajouter un poids élevé pour les coins
            else:
                move.append(self.calculate_mobility(board, color))  # Utiliser la mobilité pour pondérer le mouvement
        
        # Choisissez le meilleur coup en fonction du poids total (pions retournés + poids du coin/mobilité)
        best_move = max(valid_moves, key=lambda x: x[2] + x[3])

        return best_move[:2]  # Retourner uniquement les coordonnées x, y

    def calculate_mobility(self, board, color):
        # Calcule le nombre de mouvements légaux après un coup
        mobility = 0
        for x in range(8):
            for y in range(8):
                if board.is_legal_move(x, y, color):
                    mobility += 1
        return mobility

    # ... (le reste de la classe Bot)


class Bot:
    def __init__(self, name):
        self.name = name
    
    def check_valid_moves(self, board, color):
        valid_moves = []
        max_score = -999
        best_move = None
        
        for x in range(8):
            for y in range(8):
                if board.is_tile_empty(x, y) and board.is_legal_move(x, y, color):
                    score = self.evaluate_move(board, x, y, color)
                    if score > max_score:
                        max_score = score
                        best_move = (x, y)
                    elif score == max_score and best_move is not None:
                        best_move = random.choice([(x, y), best_move])
        
        return best_move

    def evaluate_move(self, board, x, y, color):
        score = 0
        corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
        
        # Score for capturing corners
        if (x, y) in corners:
            score += 100
        
        # Score for mobility
        score += self.calculate_mobility(board, color)
        
        # Score for flipping opponent's tiles
        flipping_score = len(board.get_flipped_tiles(x, y, color))
        score += flipping_score
        
        return score

    def calculate_mobility(self, board, color):
        mobility = 0
        for x in range(8):
            for y in range(8):
                if board.is_legal_move(x, y, color):
                    mobility += 1
        return mobility




class Bot:
    def __init__(self, name):
        self.name = name

    def alpha_beta_search(self, depth, game, alpha, beta, best_move):
        if depth == 0 or game.is_game_over:
            return self.evaluate(game), best_move

        legal_moves = self.get_legal_moves(game)

        if game.active_player == "⚪":  # Si c'est le tour du joueur blanc
            best_score = float('-inf')
            for move in legal_moves:
                game.play_move(move)
                score, _ = self.alpha_beta_search(depth - 1, game, alpha, beta, move)
                game.undo_move(move)

                if score > best_score:
                    best_score = score
                    best_move = move

                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break

            return best_score, best_move

        else:  # Si c'est le tour du joueur noir
            best_score = float('inf')
            for move in legal_moves:
                game.play_move(move)
                score, _ = self.alpha_beta_search(depth - 1, game, alpha, beta, move)
                game.undo_move(move)

                if score < best_score:
                    best_score = score
                    best_move = move

                beta = min(beta, best_score)
                if beta <= alpha:
                    break

            return best_score, best_move

    def get_legal_moves(self, game):
        # Ajoute ici la logique pour obtenir les mouvements légaux dans le jeu
        pass

    def evaluate(self, game):
        # Ajoute ici la logique pour évaluer la position du jeu
        pass



[500, -150, 30, 10, 10, 30, -150, 500,
    -150, -250, 0, 0, 0, 0, -250, -150,
    30, 0, 1, 2, 2, 1, 0, 30,
    10, 0, 2, 16, 16, 2, 0, 10,
    10, 0, 2, 16, 16, 2, 0, 10,
    30, 0, 1, 2, 2, 1, 0, 30,
    -150, -250, 0, 0, 0, 0, -250, -150,
    500, -150, 30, 10, 10, 30, -150, 500]

def check_for_valid_moves(self, main_board,main_game, depth)
from copy inport deepcopy

play_move = [[2, 4, 7],[6, 3, 7]]
if(depth > 0 ):
new_board = deepcopy(main_board)
new_game = deepcopy(main_game)
for   play_move :
    main_game.place_pawn(sauce[0], sauce[1], new_board,new_game.active_player)
    opponent_points = self.check_valid_moves(new_board,new_game)
    sauce[2] -= opponent_points

return random.choice(playable_moves)