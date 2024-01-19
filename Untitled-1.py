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

