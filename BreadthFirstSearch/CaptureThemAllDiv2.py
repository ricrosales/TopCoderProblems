'''
Problem Statement

Harry is playing magical chess. In this version of the game,
all pieces move the same way as in regular chess, but players
can cast some magical spells. Unfortunately, Harry's opponent,
Joe, has captured all of Harry's pieces except one knight; Joe,
on the other hand, still has a queen and a rook. The only chance
Harry has to win this game is to cast a spell, "Haste", that
will allow Harry's knight to make several moves in a row. You
should determine the minimal number of moves the knight needs to
capture both the rook and the queen, assuming neither of them moves.
You may capture them in either order - rook first or queen first.

You will be given a String, knight, containing information about
the knight. You will also be given a String, queen, and a String,
rook, giving you information about Joe's pieces. knight, rook and
queen will be formatted as "cr", where c is a character between 'a'
and 'h', inclusive, determining the column on the board ('a' is the
first column, 'h' is the last), and r is a digit between '1' and '8',
inclusive, determining the row (1 is the lowest, 8 is the highest).


Definition

Class:	CaptureThemAll
Method:	fastKnight
Parameters:	String, String, String
Returns:	int
Method signature:	int fastKnight(String knight, String rook, String queen)
(be sure your method is public)


Notes

-	A knight's jump moves him 2 cells along one of the axes, and 1 cell
    along the other one. In other words, if knight is in the (0,0) now, it
    can be in (-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2)
    or (1, 2) after his move.
-	The knight will capture one of Joe's pieces if it ends its move in the
    cell that the piece occupies.
-	The knight cannot jump out of the board.
-	A chessboard has 8 rows and 8 columns.


Constraints

-	knight, rook and queen will all be distinct.
-	knight, rook and queen will be formatted as "cr", where c is a lowercase
    character between 'a' and 'h', inclusive, and r is a digit between '1' and
    '8', inclusive.


Examples

0)

"a1"
"b3"
"c5"
Returns: 2
From "a1", the knight can move directly to "b3" and capture the rook. From
there, the knight can move directly to "c5" and capture the queen.

1)

"b1"
"c3"
"a3"
Returns: 3
The rook and the queen are both 1 move away from the knight. Once the knight
captures one of them (it doesn't matter which one), it can return to its
starting location, and capture the other piece in one more move.

2)

"a1"
"a2"
"b2"
Returns: 6
The rook and the queen are close, but it takes 6 moves to capture them.

3)

"a5"
"b7"
"e4"
Returns: 3

4)

"h8"
"e2"
"d2"
Returns: 6

'''


class CaptureThemAll:

    @staticmethod
    def gen_paths(cur_pos, rook, queen):
        paths = []
        cur_pos[1]['moves'] += 1
        for i in [-2, -1, 1, 2]:
            if 97 <= ord(cur_pos[0][0]) + i <= 104:
                for j in [-2, -1, 1, 2]:
                    if 1 <= int(cur_pos[0][1]) + j <= 8:
                        if not i * j in [-4, -1, 1, 4]:
                            new_dict = cur_pos[1].copy()
                            new = chr(ord(cur_pos[0][0]) + i) + str(int(
                                cur_pos[0][1]) + j)
                            if new == rook:
                                new_dict['rook'] = True
                            if new == queen:
                                new_dict['queen'] = True
                            paths.append([new, new_dict])
        return paths

    @staticmethod
    def fastKnight(knight, rook, queen):

        knight = [knight, {'moves': 0, 'rook': False, 'queen': False}]
        frontier = CaptureThemAll.gen_paths(knight, rook, queen)

        while frontier:
            cur_pos = frontier.pop(0)
            if cur_pos[1]['rook'] and cur_pos[1]['queen']:
                return cur_pos[1]['moves']
            else:
                frontier.extend(CaptureThemAll.gen_paths(cur_pos, rook, queen))
        return None

if __name__ == '__main__':

    cta = CaptureThemAll()
    # 2
    print(cta.fastKnight("a1", "b3", "c5"))
    # 3
    print(cta.fastKnight('b1', 'c3', 'a3'))
    # 6
    print(cta.fastKnight("a1", "a2", "b2"))
    # 3
    print(cta.fastKnight("a5", "b7", "e4"))
    # 6
    print(cta.fastKnight("h8", "e2", "d2"))
