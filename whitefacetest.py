from minx import Minx
from whitestar import white_star
from whitecorners import white_corners

thing = Minx()
solution = []

#test entire white cross
scramble = thing.scramble()
print("scramble\n")
print(scramble)
print("\n")
thing.print_state()
print("\n")
solution = white_star(thing)
print("testing white corners\n\n\n\n\n\n\n\n")
solution = white_corners(thing, solution)
thing.print_state()
print("\n")
# print(solution)
