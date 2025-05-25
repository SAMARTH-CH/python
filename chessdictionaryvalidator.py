print('samarth\n1AY24AI097')
def is_valid_chess_board(board):
    piece_counts = {}
    white_king = 0
    black_king = 0
    valid_columns = 'abcdefgh'
    valid_rows = '12345678'

    for position, piece in board.items():
        if len(position) != 2 or position[0] not in valid_rows or position[1] not in valid_columns:
            print(f"Invalid position: {position}")
            return False
        piece_counts[piece] = piece_counts.get(piece, 0) + 1
    white_king = piece_counts.get('wking', 0)
    black_king = piece_counts.get('bking', 0)

    if white_king != 1 or black_king != 1:
        print("Invalid number of kings.")
        return False
    white_pieces = sum(count for piece, count in piece_counts.items() if piece.startswith('w'))
    black_pieces = sum(count for piece, count in piece_counts.items() if piece.startswith('b'))

    if white_pieces > 16 or black_pieces > 16:
        print("Too many pieces for one player.")
        return False

    if piece_counts.get('wpawn', 0) > 8 or piece_counts.get('bpawn', 0) > 8:
        print("Too many pawns.")
        return False

    print("The chess board is valid.")
    return True
chess_board = {
    '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen',
    '3e': 'wking', '2h': 'wpawn', '4d': 'wpawn', '5e': 'wpawn',
    '6d': 'wpawn', '7e': 'wpawn', '8e': 'wpawn', '1a': 'wrook'
}

is_valid_chess_board(chess_board)
