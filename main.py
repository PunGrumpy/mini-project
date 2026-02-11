#!/usr/bin/env python3
from checkmate import checkmate

example_1 = """\
R...
.K..
..P.
....\
"""
example_2 = """\
..
.K\
"""


def main():
    board = example_1
    checkmate(board)


if __name__ == "__main__":
    main()
