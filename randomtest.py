from minx import Minx
from randommoves import move_edge, move_corner


thing = Minx()

# #test move edge
# #i think this works
# thing.scramble()
# piece1 = (0, 1)
# target1 = (0, 1)

# solution = move_edge(thing, piece1, target1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 20)
# print(solution)
# thing.print_state()

#test move corner
#i think this works too
# thing.white0(1)
# thing.darkgreen5(-1)
scramble = thing.scramble()
print(scramble)
# thing.purple4(2)
# thing.lightgreen11(-2)
# thing.lightblue8(2)
# thing.red1(-2)
# thing.darkblue2(-2)
# thing.orange7(-2)
# thing.gray6(-2)
# thing.purple4(2)
thing.print_state()
print(thing.corners[(0, 5, 1)])

piece = (0, 5, 1)
target = (0, 5, 1)

solution = move_corner(thing, piece, target, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 8)
print(solution)
print(thing.corners[(0, 5, 1)])
thing.print_state()