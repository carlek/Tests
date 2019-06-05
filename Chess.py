import random

class ChessGame:

    def __init__(self):
        # position a1->h8
        # player and piece:  [b|w]C   black or white and Piece (K,Q, etc)
        # key is position. value is piece
        self.board = {'a1':'wR', 'b1':'wN', 'c1':'wB', 'd1':'wQ', 'e1':'wK', 'f1':'wB', 'g1':'wN', 'h1':'wR',
                      'a2':'wP', 'b2':'wP', 'c2':'wP', 'd2':'wP', 'e2':'wP', 'f2':'wP', 'g2':'wP', 'h2':'wP',
                      'a7':'bP', 'b7':'bP', 'c7':'bP', 'd7':'bP', 'e7':'bP', 'f7':'bP', 'g7':'bP', 'h7':'bP',
                      'a8':'bR', 'b8':'bN', 'c8':'bB', 'd8':'bQ', 'e8':'bK', 'f8':'bB', 'g8':'bN', 'h8':'bR'}

        self.white_captured = []
        self.black_captured = []
        self.winner = None

    def remove_piece(self, position):
        """
        remove a piece after capture.
        :param position: string key into board dict
        :return:
        """
        if self.board[position][0] == 'w':
            self.black_captured.append(self.board[position])
        else:
            self.white_captured.append(self.board[position])
        del self.board[position]

    @staticmethod
    def get_valid_moves(piece, position):
        """
        :param piece: string
        :param position: string key into board dict
        :return:
        """
        if piece == 'K':
            return valid_moves_for_king(position)
        elif piece == 'Q':
            return valid_moves_for_queen(position)
        elif piece == 'B':
            return valid_moves_for_bishop(position)
        elif piece == 'N':
            return valid_moves_for_knight(position)
        elif piece == 'R':
            return valid_moves_for_rook(position)
        elif piece == 'P':
            return valid_moves_for_pawn(position)

    def pick_move(self, valid_moves, piece, have_brain=True):
        """
        pick a move
        :param valid_moves: list of string keys into board dict
        :param piece: string piece
        :param have_brain:  boolean true for smart move, false for random
        :return:
        """
        if have_brain:
            new_position = self.brainy_move(valid_moves, piece)
        else:
            new_position = random.choice(valid_moves)
        return new_position

    def brainy_move(self, valid_moves, piece):
        """
        :param valid_moves:
        :param piece:
        :return:
        """
        #TODO some intelligence needed
        return ''

    def is_captured(self, position, player):
        """
        is the move a capture return true if so false if not
        position: string key into board dict
        player: string w or b
        """
        if position in self.board.keys() and self.board[position][0] != player:
            return True
        else:
            return False

    def perform_move(self, old_position, player):
        """
        for a particular player perform a move
        :param old_position: string key into board dict
        :param player:  string w or b
        :return:
        """
        piece = self.board[old_position]
        valid_moves = self.get_valid_moves(piece[1], old_position)
        new_position = self.pick_move(self, valid_moves, piece)
        if self.is_captured(new_position, player):
            self.remove_piece(new_position)
        self.board[new_position] = piece

    def play(self, player):
        """
        select a move and play it for a player
        :param player: string w or b
        :return:
        """
        available_to_play = self.get_all_positions(player)
        position_to_play = random.choice(available_to_play)
        perform_move(position_to_play, player)


if __name__ == '__main__':
    # start a game with a fresh board
    current_game = ChessGame()

    # play white, black until a winner or a stalemate
    while not current_game.winner:
        current_game.play('w')
        if not current_game.winner:
            current_game.play('b')

    print(current_game.winner)
