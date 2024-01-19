# À l'intérieur de la classe Bot:
# ...

def check_valid_moves(self, board, color):
    # ... (le reste du code précédent)
    
    # Ajouter une vérification pour les coins pour augmenter leur priorité
    for move in valid_moves:
        x_pos, y_pos = move[0], move[1]
        if (x_pos, y_pos) in [(0, 0), (0, 7), (7, 0), (7, 7)]:
            move.append(1000)  # Ajouter un poids élevé pour les coins
        else:
            move.append(new_board.board[tile_index].weight)
    
    # ... (le reste du code précédent)

def calculate_mobility(self, board, color):
    # Calcule le nombre de mouvements légaux après un coup
    mobility = 0
    for x in range(8):
        for y in range(8):
            if board.is_legal_move(x, y, color):
                mobility += 1
    return mobility

# ...

# Lors de la sélection du mouvement:
# Ajoutez un poids basé sur la mobilité
if total_flipped + mobility_weight * self.calculate_mobility(board, color) > max_pawns_flipped:
    # ... (le reste du code précédent)
