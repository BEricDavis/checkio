# Chess is a two-player strategy game played on a checkered game board laid out in eight rows (called ranks and
# denoted with numbers 1 to 8) and eight columns (called files and denoted with letters a to h) of squares.
# Each square of the chessboard is identified by a unique coordinate pair -- a letter and
# a number (ex, "a1", "h8", "d6"). For this mission we only need to concern ourselves with pawns.
# A pawn may capture an opponent's piece on a square diagonally in front of it on an adjacent file, by moving to
# that square. For white pawns the front squares are squares with greater row than their.
# A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall.
# With this strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square.
# We have several white pawns on the chess board and only white pawns. You should design your code to find how
# many pawns are safe.
# You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.
# Input: Placed pawns coordinates as a set of strings.
# Output: The number of safe pawns as a integer.


def safe_pawns(pawns):
    defended = set()
    count = 0
    for p in pawns:
        defended.add(''.join((chr(ord(p[0])+1), str(int(p[1]) + 1))))
        defended.add(''.join((chr(ord(p[0])-1), str(int(p[1]) + 1))))

    for p in pawns:
        if p in defended:
            count += 1

    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
