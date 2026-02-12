def checkmate(board: str):
    parsed = parse_board(board)

    if not validate_board(parsed):
        print("Fail")
        return

    king_position = find_king(parsed)

    if king_position is None:
        print("Fail")
        return

    if is_king_in_check(parsed,king_position):
        print("Success")
    else:
        print("Fail")

    return print(king_position)


def parse_board(board_str: str) -> list | None:
    if not isinstance(board_str, str):
        return None

    rows = board_str.splitlines()
    rows = [row for row in rows if row.strip() != ""]  # Remove empty lines

    # 2D list
    board = [list(row) for row in rows]
    return board


def validate_board(board) -> bool:
    # IMPORTANT: Must be list and not empty
    if not isinstance(board, list) or len(board) == 0:
        return False

    size = len(board)

    king_count = 0

    for row in board:
        if not isinstance(row, list):
            return False

        # IMPORTANT: Must be square
        if len(row) != size:
            return False

        for cell in row:
            if cell == "K":
                king_count += 1

    # IMPORTANT: Must have exactly one king
    if king_count != 1:
        return False

    return True


def find_king(board):
    # IMPORTANT: Must be list
    if not isinstance(board, list):
        return None

    # NOTE: enumerate gives index and value
    for i, row in enumerate(board):
        # IMPORTANT: Each row must be list
        if not isinstance(row, list):
            return None

        for j, col in enumerate(row):
            if col == "K":
                return (i, j)

    return None


# TODO: Check if the king is in checkmate (is_king_in_check function)
def is_king_in_check(board,king_position) -> bool:
    size = len(board)
    king_row, king_col = king_position

    # check if king is in checkmate
    # travel every row and column in board to find a piece
    for row in range(size):
        for col in range(size):
            piece = board[row][col]
            # check if the piece is a pawn
            if piece == "P":
                if pawn_attacks(row, col, king_row, king_col):
                    return True
            # check if the piece is a bishop
            elif piece == "B":
                if bishop_attacks(board, row, col, king_row, king_col):
                    return True
            # check if the piece is a rook
            elif piece == "R":
                if rook_attacks(board, row, col, king_row, king_col):
                    return True
            # check if the piece is a queen
            elif piece == "Q":
                if queen_attacks(board, row, col, king_row, king_col):
                    return True

    return False

"""
. . . . . . .
. . . . . . .
. . X . K . .  k_row = 2, k_col = 4
. . . P . . .  p_row = 3, p_col = 3
. . . . . . .  is_row_above = true -> (p_row - 1 == k_row)
. . . . . . .  is_diagonal = true -> (abs(p_col - k_col) == 1)
. . . . . . .
"""
def pawn_attacks( p_row, p_col, k_row, k_col) -> bool:
    is_row_above = p_row - 1 == k_row
    is_diagonal = abs(p_col - k_col) == 1

    if is_row_above and is_diagonal:
        return True
    else:
        return False

""" 
X . . . . . X  
. X . . . K .  k_row = 1, k_col = 5
. . X . X . .
. . . B . . .  b_row = 3, b_col = 3
. . X . X . .
. X . . . X .  row_diff = 2, col_diff = 2 -> king in line move of bishop
X . . . . . X
"""
def bishop_attacks(board, b_row, b_col, k_row, k_col) -> bool:
    row_diff = abs(b_row - k_row)
    col_diff = abs(b_col - k_col)

    if row_diff == col_diff:
        return is_path_clear(board, b_row, b_col, k_row, k_col)
    else:
        return False


"""
. . . X . . .
. . . K . . .   k_row = 1, k_col = 3
. . . X . . .   
X X X R X X X   r_row = 3, r_col = 3
. . . X . . .   
. . . X . . .   r_col == k_col -> true
. . . X . . .   r_row == k_row -> false
"""
def rook_attacks(board, r_row, r_col, k_row, k_col) -> bool:
    # check if rook in same row or column as king
    if r_row == k_row or r_col == k_col:
        return is_path_clear(board, r_row, r_col, k_row, k_col)
    else:
        return False

def queen_attacks(board, q_row, q_col, k_row, k_col) -> bool:
    # queen can use logic of rook or bishop
    if rook_attacks(board, q_row, q_col, k_row, k_col):
        return True
    if bishop_attacks(board, q_row, q_col, k_row, k_col):
        return True
    return False


def is_path_clear(board, piece_row, piece_col, king_row, king_col) -> bool:
    # find row direction from piece to king
    if king_row > piece_row:
        step_row = 1  
    elif king_row < piece_row:
        step_row = -1  
    else:
        step_row = 0  

    # find col direction from piece to king
    if king_col > piece_col:
        step_col = 1  
    elif king_col < piece_col:
        step_col = -1  
    else:
        step_col = 0  

    # start check in next move
    current_row = piece_row + step_row
    current_col = piece_col + step_col

    while current_row != king_row or current_col != king_col:
        # check if attack other piece
        if board[current_row][current_col] != ".":
            return False  
        # move to next position
        current_row = current_row + step_row
        current_col = current_col + step_col

    return True
