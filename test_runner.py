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
    # 1️⃣ 1x1 with King
    ("K", "Fail", "1x1 only King"),
    # 2️⃣ 1x1 without King
    (".", "Fail", "1x1 no King"),
    # 3️⃣ Multiple Kings
    ("KK\nKK", "Fail", "Multiple Kings"),
    # 4️⃣ Non-square board
    ("R...\n.K..\n..P.", "Fail", "Non-square board"),
    # 5️⃣ Empty string
    ("", "Fail", "Empty string"),
    # 6️⃣ Valid no attack
    ("R...\n.K..\n..P.\n....", "Fail", "Valid board no check"),
    # 7️⃣ Rook horizontal check
    ("R.K\n...\n...", "Success", "Rook horizontal check"),
    # 8️⃣ Rook vertical check
    ("R..\n...\nK..", "Success", "Rook vertical check"),
    # 9️⃣ Rook blocked
    ("RPK\n...\n...", "Fail", "Rook blocked"),
    # 🔟 Bishop check
    ("B..\n.K.\n...", "Success", "Bishop diagonal check"),
    # 1️⃣1️⃣ Bishop blocked
    ("B..\n.P.\n.K.", "Fail", "Bishop blocked"),
    # 1️⃣2️⃣ Queen check (diagonal)
    ("Q..\n.K.\n...", "Success", "Queen diagonal check"),
    # 1️⃣3️⃣ Queen check (horizontal)
    ("Q.K\n...\n...", "Success", "Queen horizontal check"),
    # 1️⃣4️⃣ Pawn check (correct direction)
    ("...\n.P.\nK..", "Success", "Pawn diagonal attack"),
    # 1️⃣5️⃣ Pawn wrong direction
    ("K..\n.P.\n...", "Fail", "Pawn wrong direction"),
    # 1️⃣6️⃣ Pawn blocked
    ("...\n.P.\n.PK", "Fail", "Pawn not aligned diagonally"),
]


for board, expected, name in tests:
    run_test(board, expected, name)
