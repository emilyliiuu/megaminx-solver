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

solution = []
new_state = {0: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             1: [1, 1, 1, 1, 11, 10, 10, 8, 2, 1], 
             2: [2, 2, 2, 2, 11, 11, 8, 11, 5, 2], 
             3: [3, 3, 3, 3, 1, 5, 7, 1, 2, 3], 
             4: [4, 4, 4, 4, 10, 3, 8, 10, 7, 4], 
             5: [5, 5, 5, 5, 4, 6, 1, 9, 3, 5], 
             6: [9, 6, 11, 7, 5, 11, 9, 8, 11, 10], 
             7: [7, 9, 6, 8, 7, 7, 1, 10, 3, 7], 
             8: [8, 6, 8, 4, 9, 7, 8, 2, 6, 6], 
             9: [4, 11, 7, 9, 6, 9, 2, 1, 10, 8], 
             10: [6, 10, 10, 5, 9, 3, 10, 7, 11, 6], 
             11: [6, 11, 3, 4, 4, 8, 9, 2, 5, 9]}
thing.set_state(new_state)

# print("solving first layer edges")
# solution = firstlayeredges(thing, solution)
# print("\n")

# solution = []
# print("SOLVING FROM HERE")
# thing.print_state()
# print("\n\n\n\n\n")

print("solving insert corners\n\n\n\n\n\n\n\n")
solution = insert_corners(thing, solution)
print("\n")

print("solving insert edges\n\n\n\n\n\n\n\n")
solution = insert_edges(thing, solution)
print("\n")


print("solving second half corners")
solution = secondhalfcorners(thing, solution)
print("\n")

print("solving second half edges")
solution = secondhalfedges(thing, solution)
print("\n")

print("solving last layer")
solution = lastlayer(thing, solution)
print("\n")

thing.print_state()
print("\n")
print(solution)
print(len(solution))

solution = fixsolution(solution)
print(solution)
