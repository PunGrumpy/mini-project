def checkmate(board: str):
    parsed = parse_board(board)

    if not validate_board(parsed):
        print("Fail")
        return

    return print("Valid")


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
