def checkmate(board: str):
    parsed = parse_board(board)
    return parsed


def parse_board(board_str: str) -> list | None:
    if not isinstance(board_str, str):
        return None

    rows = board_str.splitlines()
    rows = [row for row in rows if row.strip() != ""]  # Remove empty lines

    # 2D list
    board = [list(row) for row in rows]
    return board
