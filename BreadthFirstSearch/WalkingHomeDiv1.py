'''
Problem Statement


Johnny has to walk home from school, and wants to map out the best route to take, so that he has to cross as few streets as possible.

You are given a String[] map that maps the roadway layout of Johnny's town. The location of Johnny's school is designated with a 'S' character, and the location of Johnny's home is designated with a 'H' character. North-South roads are denoted by a '|' character, while East-West roads are denoted by a '-' character. Intersections, which can never be crossed, are indicated by '*' characters. Fences, indicated by a 'F' character, can also never be crossed. All other areas are indicated by '.' characters; Johnny can walk freely over these areas.

For maximum safety, Johnny may only walk directly across a road, perpendicular to the traffic, never diagonally. All of Johnny's movements, onto and off of a road, and walking around town, should be in one of the four cardinal directions. Johnny may, however, cross roads that are multiple lanes wide, and doing so only counts as a single crossing. Two or more adjacent || characters are always considered to be a single road, and this works similarly for '-' characters that appear adjacent vertically.

For instance, the following requires only a single crossing, since it's a single two-lane road:

S.||.H
Also, a situation such as the following leaves Johnny with no safe way to walk home, since he cannot cross the road diagonally, and can only step onto and off a road in a direction perpendicular to the road:

S||
||H
Also notice that because Johnny can never move diagonally, in the following case, Johnny cannot get home:

S.F
.F.
F.H
You are to return an int indicating the fewest number of times Johnny must cross the street on his way home. If there is no safe way for Johnny to get home, return -1.


Definition


Class:	WalkingHome
Method:	fewestCrossings
Parameters:	String[]
Returns:	int
Method signature:	int fewestCrossings(String[] map)
(be sure your method is public)


Notes

-	If a street is more than one unit wide, it still only counts as a single crossing.

Constraints

-	map will contain between 1 and 50 elements, inclusive.
-	Each element of map will contain between 1 and 50 characters, inclusive.
-	Each element of map will contain only the characters '.', '-', '|', '*', 'F', 'S', 'H'.
-	There will be exactly one occurrence each of 'S' and 'H' in map.
-	Each element of map will contain the same number of characters.

Examples

0)

{"S.|..",
 "..|.H"}
Returns: 1
Here, Johnny lives right across the street from the school, so inevitably, he's crossing the street once to get home.
1)

{"S.|..",
 "..|.H",
 "..|..",
 "....."}
Returns: 0
Similar to above, but since the road has a dead end (maybe even a cul-de-sac at the end), Johnny can get home without actually having to cross the road.
2)

{"S.||...",
 "..||...",
 "..||...",
 "..||..H"}
Returns: 1
Notice here that even though it's a 2-lane highway, it only counts as a single crossing.
3)

{"S.....",
 "---*--",
 "...|..",
 "...|.H"}
Returns: 1
Here, Johnny could go down across the street and then right across another street to his house. However, if he first goes to the right before crossing down, he will only cross 1 street.
4)

{"S.F..",
 "..F..",
 "--*--",
 "..|..",
 "..|.H"}
Returns: 2
Similar to above, but because there's a fence around the school, Johnny has no choice but to cross twice.
5)

{"H|.|.|.|.|.|.|.|.|.|.|.|.|.",
 "F|F|F|F|F|F|F|F|F|F|F|F|F|-",
 "S|.|.|.|.|.|.|.|.|.|.|.|.|."}
Returns: 27
Poor Johnny lives so close to school, but that fence makes him cross the street quite a bit just to get home.
6)

{"S-H"}
Returns: -1

'''