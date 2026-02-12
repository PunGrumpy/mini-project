from checkmate import checkmate


def run_test(board, expected, name):
    print(f"{name}")
    print("Board:")
    print(board if board else "(empty string)")
    print("Expected:", expected)
    print("Result:  ", end="")
    checkmate(board)
    print("—" * 30)


tests = [
    # NOTE 1x1 board
    ("K", "Fail", "1x1 only King"),
    (".", "Fail", "1x1 no King"),
    # NOTE 2x2 board
    ("K.\n..", "Fail", "2x2 no attack"),
    ("RK\n..", "Success", "2x2 rook check"),
    ("B.\n.K", "Success", "2x2 bishop diagonal check"),
    # NOTE No King
    ("R..\n...\n..P", "Fail", "No King on board"),
    # NOTE Multiple Kings
    ("K.K\n...\nK..", "Fail", "Multiple Kings"),
    # NOTE Non-square board
    ("R...\n.K..\n..P.", "Fail", "Non-square board"),
    ("", "Fail", "Empty string board"),
    # NOTE Blocked attack cases
    ("RPK\n...\n...", "Fail", "Rook blocked horizontal"),
    ("R..\nP..\nK..", "Fail", "Rook blocked vertical"),
    ("B..\n.P.\n.K.", "Fail", "Bishop blocked diagonal"),
    ("Q..\n.P.\n.K.", "Fail", "Queen blocked diagonal"),
]

for board, expected, name in tests:
    run_test(board, expected, name)
