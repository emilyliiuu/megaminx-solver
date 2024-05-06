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
print(thing.edges)

new_state = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
            [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [11, 11, 11, 11, 11, 11, 11, 11, 11, 11]]

thing.set_state(new_state)
thing.print_state()
print(thing.edges)
