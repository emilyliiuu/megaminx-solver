from minx import Minx
from whitestar import white_star
from whitecorners import white_corners
from firstlayeredges import firstlayeredges
from upsidedowntriangles import insert_corners, insert_edges
from secondhalfcorners import secondhalfcorners
from secondhalfedges import secondhalfedges
from lastlayer import lastlayer
from fixsolution import fixsolution

thing = Minx()


scramble = thing.scramble()
print("scramble\n")
print(scramble)
print("\n")
thing.print_state()
print("\n")

print("testing white star\n\n\n\n\n\n\n\n")
solution = white_star(thing)
print("\n")

print("testing white corners\n\n\n\n\n\n\n\n")
solution = white_corners(thing, solution)
print("\n")

while thing.state[0] != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
    solution = []
    print("generating new scramble")
    thing.scramble()
    print("testing white star\n\n\n\n\n\n\n\n")
    solution = white_star(thing)
    print("\n")

    print("testing white corners\n\n\n\n\n\n\n\n")
    solution = white_corners(thing, solution)
    print("\n")

print("testing first layer edges")
solution = firstlayeredges(thing, solution)
print("\n")

print(thing.state)

solution = []
print("SOLVING FROM HERE")
thing.print_state()
print("\n\n\n\n\n")

print("testing insert corners\n\n\n\n\n\n\n\n")
solution = insert_corners(thing, solution)
print("\n")

print("testing insert edges\n\n\n\n\n\n\n\n")
solution = insert_edges(thing, solution)
print("\n")

print("testing second half corners")
solution = secondhalfcorners(thing, solution)
print("\n")

print("testing second half edges")
solution = secondhalfedges(thing, solution)
print("\n")

print("testing last layer")
solution = lastlayer(thing, solution)
print("\n")

thing.print_state()
print("\n")
print(solution)
print(len(solution))

solution = fixsolution(solution)
print(solution)