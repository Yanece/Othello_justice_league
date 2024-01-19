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
