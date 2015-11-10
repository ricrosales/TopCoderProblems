'''
Problem Statement


You are in a maze containing revolving doors. The doors can be turned 90
degrees by pushing against them in either direction. You are to find a route
from the start square to the end square that involves revolving as few doors as
possible. Given a map of the maze, determine the fewest number of door
revolutions necessary to get from the start to the end.

In the map:

   ' ': empty space
   '#': wall
   'O': center of a revolving door (letter "oh", not zero)
   '-': horizontal door (always adjacent to a 'O')
   '|': vertical door (always adjacent to a 'O')
   'S': start square
   'E': end square
Each revolving door will always be oriented horizontally (with two horizontal
segments) or vertically (with two vertical segments):

    |
    O  or  -O-
    |
Doors can be revolved 90 degrees by moving onto a door segment from any of the
4 squares diagonally adjacent to the door center, i.e., the 'X' characters
below:

   X|X     X X
    O  or  -O-
   X|X     X X
Here is an example map:

        ###
        #E#
       ## #
    ####  ##
    # S -O-#
    # ###  #
    #      #
    ########
In this example, 2 door revolutions are necessary to get from 'S' to 'E'. The
first turn is shown here:

        ###         ###
        #E#         #E#
       ## #        ## #
    ####  ##    #### |##
    # S -O-#    # S  OX#
    # ### X#    # ###| #
    #      #    #      #
    ########    ########
And the second turn is shown here:

        ###         ###
        #E#         #E#
       ## #        ## #
    ####X|##    #### X##
    # S  O #    # S -O-#
    # ###| #    # ###  #
    #      #    #      #
    ########    ########
Your method should return an int, the minimum number of door revolutions
necessary to get from the start square to the end square. If there is no way to
reach the end square, return -1.


Definition


Class:	RevolvingDoors
Method:	turns
Parameters:	String[]
Returns:	int
Method signature:	int turns(String[] map)
(be sure your method is public)


Notes

-	Assume that all squares off the edge of the map are walls.

Constraints

-	map will contain between 3 and 50 elements, inclusive.
-	Each element of map will contain between 3 and 50 characters, inclusive.
-	Each element of map will contain the same number of characters.
-	Each character in map will be one of 'S', 'E', 'O', '-', '|', '#', and ' '
    (space).
-	There will be exactly one 'S' and one 'E' in map.
-	There will be between 1 and 10 doors, inclusive, and they will be formatted
    in map as described in the problem statement.
-	No two doors will be close enough for any part of them to occupy the same
    square.
-	It is not allowed for a door to be blocked and unable to turn. There will
    not be any walls in any of the 4 squares immediately adjacent to the center
    of a door, nor will a door be on the edge of the map.

Examples

0)

{ "    ### ",
  "    #E# ",
  "   ## # ",
  "####  ##",
  "# S -O-#",
  "# ###  #",
  "#      #",
  "########" }
Returns: 2
This is the example from the problem statement.
1)

{ "#### ",
  "#S|##",
  "# O #",
  "##|E#",
  " ####" }
Returns: -1
There is no way to reach the end square.
2)

{ " |  |  |     |  |  |  |  |  | ",
  " O  O EO -O- O  O  O  O  OS O ",
  " |  |  |     |  |  |  |  |  | " }
Returns: 7
The optimal path involves turning the 3rd door twice, and the 5th, 6th, 7th,
8th, and 9th doors once each (counting from the left). Note that the 'S' and
'E' do not block doors, and in fact you must turn the 3rd door twice to end
up on the 'E'.
3)

{ "###########",
  "#    #    #",
  "#  S | E  #",
  "#    O    #",
  "#    |    #",
  "#         #",
  "###########" }
Returns: 0
4)

{ "        E",
  "    |    ",
  "    O    ",
  "    |    ",
  " -O-S-O- ",
  "    |    ",
  "    O    ",
  "    |    ",
  "         " }
Returns: -1
You are stuck, unable to move or turn any doors from this position.
5)

{ "##E#   ",
  "#  ##  ",
  " -O-## ",
  " #  ## ",
  " ##  ##",
  "  -O-  ",
  "##  ## ",
  " # ### ",
  " #  S  " }
Returns: 5
6)

{ "#############",
  "#  #|##|#   #",
  "#   O  O    #",
  "# E || || S #",
  "#    O  O   #",
  "#   #|##|#  #",
  "#############" }
Returns: 4
After all the doors have been turned, the map looks like this:
    #############
    #  # ## #   #
    #  -O--O-   #
    # E       S #
    #   -O--O-  #
    #   # ## #  #
    #############
'''

from copy import deepcopy


class RevolvingDoors:

    @staticmethod
    def vert_door(amap, i):

        amap[i[0]][i[1]] = ' '

        if amap[i[0] + 1][i[1]] == 'O':

            amap[i[0] + 2][i[1]] = ' '
            if amap[i[0] + 1][i[1] + 1] not in ['E', 'S']:
                amap[i[0] + 1][i[1] + 1] = '-'
            if amap[i[0] + 1][i[1] - 1] not in ['E', 'S']:
                amap[i[0] + 1][i[1] - 1] = '-'

        elif amap[i[0] - 1][i[1]] == 'O':

            amap[i[0] - 2][i[1]] = ' '
            if amap[i[0] - 1][i[1] - 1] not in ['E', 'S']:
                amap[i[0] - 1][i[1] - 1] = '-'
            if amap[i[0] - 1][i[1] + 1] not in ['E', 'S']:
                amap[i[0] - 1][i[1] + 1] = '-'

        return amap

    @staticmethod
    def horiz_door(amap, i):

        amap[i[0]][i[1]] = ' '

        if amap[i[0]][i[1] + 1] == 'O':
            amap[i[0]][i[1] + 2] = ' '
            if amap[i[0] + 1][i[1] + 1] not in ['E', 'S']:
                amap[i[0] + 1][i[1] + 1] = '|'
            if amap[i[0] - 1][i[1] + 1] not in ['E', 'S']:
                amap[i[0] - 1][i[1] + 1] = '|'

        elif amap[i[0]][i[1] - 1] == 'O':
            amap[i[0]][i[1] - 2] = ' '
            if amap[i[0] + 1][i[1] - 1] not in ['E', 'S']:
                amap[i[0] + 1][i[1] - 1] = '|'
            if amap[i[0] - 1][i[1] - 1] not in ['E', 'S']:
                amap[i[0] - 1][i[1] - 1] = '|'

        return amap

    @staticmethod
    def update_pos(cur_pos, dest_pos, amap):

        if amap[cur_pos['row']][cur_pos['col']] not in ['E', 'S']:
            amap[cur_pos['row']][cur_pos['col']] = ' '
        if amap[dest_pos['row']][dest_pos['col']] not in ['E', 'S']:
            amap[dest_pos['row']][dest_pos['col']] = 'X'

        return amap

    @staticmethod
    def gen_paths(cur_pos, visited):

        paths = []

        for i in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            cur_map = deepcopy(cur_pos['map'])
            try:
                new_pos = cur_map[cur_pos['row'] + i[0]][cur_pos['col'] + i[1]]
            except IndexError:
                continue
            p = (cur_pos['row'] + i[0], cur_pos['col'] + i[1])
            if p[0] < 0 or p[1] < 0:
                continue
            if p not in visited:
                visited.append(p)
                if new_pos not in ['#', 'O']:
                    if new_pos == '|' and i not in [(1, 0), (-1, 0)]:
                        m = RevolvingDoors.vert_door(cur_map, p)
                        dest_pos = {'row': cur_pos['row'] + i[0],
                                    'col': cur_pos['col'] + i[1],
                                    'turns': cur_pos['turns'] + 1,
                                    'end': False}
                        m = RevolvingDoors.update_pos(cur_pos, dest_pos, m)
                        dest_pos['map'] = m
                        paths.append(dest_pos)
                    elif new_pos == '-' and i not in [(0, 1), (0, -1)]:
                        m = RevolvingDoors.horiz_door(cur_map, p)
                        dest_pos = {'row': cur_pos['row'] + i[0],
                                    'col': cur_pos['col'] + i[1],
                                    'turns': cur_pos['turns'] + 1,
                                    'end': False}
                        m = RevolvingDoors.update_pos(cur_pos, dest_pos, m)
                        dest_pos['map'] = m
                        paths.append(dest_pos)
                    elif new_pos == 'E':
                        dest_pos = {'row': cur_pos['row'] + i[0],
                                    'col': cur_pos['col'] + i[1],
                                    'turns': cur_pos['turns'],
                                    'end': True}
                        m = RevolvingDoors.update_pos(cur_pos, dest_pos, cur_map)
                        dest_pos['map'] = m
                        paths.append(dest_pos)
                    elif new_pos in [' ', 'S']:
                        dest_pos = {'row': cur_pos['row'] + i[0],
                                    'col': cur_pos['col'] + i[1],
                                    'turns': cur_pos['turns'],
                                    'end': False}
                        m = RevolvingDoors.update_pos(cur_pos, dest_pos, cur_map)
                        dest_pos['map'] = m
                        paths.extend(RevolvingDoors.gen_paths(dest_pos,
                                                              visited))

        return paths

    @staticmethod
    def turns(amap):

        m = []
        for r in amap:
            m.append(list(r))

        for r in range(len(m)):
            try:
                ind = m[r].index('S')
                if ind != -1:
                    start_pos = {'row': r, 'col': ind, 'turns': 0, 'end': False,
                                 'map': m}
                    frontier = [start_pos]
                    break
            except ValueError:
                continue

        while frontier:
            cur_pos = frontier.pop(0)
            if cur_pos['end']:
                # for r in cur_pos['map']:
                #     print(''.join(r))
                return cur_pos['turns']
            coord = (cur_pos['row'], cur_pos['col'])
            frontier.extend(RevolvingDoors.gen_paths(cur_pos, [coord]))

        return -1

if __name__ == '__main__':

        rd = RevolvingDoors()
        # 4
        l = ["#############",
             "#  #|##|#   #",
             "#   O  O    #",
             "# E || || S #",
             "#    O  O   #",
             "#   #|##|#  #",
             "#############"]
        print(rd.turns(l))
        # 5
        l = ["##E#   ",
             "#  ##  ",
             " -O-## ",
             " #  ## ",
             " ##  ##",
             "  -O-  ",
             "##  ## ",
             " # ### ",
             " #  S  "]
        print(rd.turns(l))
        # 2
        l = ["    ### ",
             "    #E# ",
             "   ## # ",
             "####  ##",
             "# S -O-#",
             "# ###  #",
             "#      #",
             "########"]
        print(rd.turns(l))
        # -1
        l = ["        E",
             "    |    ",
             "    O    ",
             "    |    ",
             " -O-S-O- ",
             "    |    ",
             "    O    ",
             "    |    ",
             "         "]
        print(rd.turns(l))
        # 0
        l = ["###########",
             "#    #    #",
             "#  S | E  #",
             "#    O    #",
             "#    |    #",
             "#         #",
             "###########"]
        print(rd.turns(l))
