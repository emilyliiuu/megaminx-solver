from minx import Minx
from randommoves import move_corner

'''
PLAN:
move corners to right spot (above slot) using bfs probably
insert using one of three cases:
1. white facing right
2. white facing up
3. white facing left

todo:
find out how to move corners to right place
check which direction white faces
    may need to change rotation of corners in minx to standardize orientation
determine which faces make up r, u, f (not using l moves because they are annoying)
algorithms to insert
    1. R U R'
    2. R U2 R' U' R U R'
    3. U R U' R'
loop through all 5 corners

'''
solution = []
#moving corners to right place (above correct slot)
######TODO#############
#may need to check if corner piece is already in a white corner slot?
#just take it out and then move to right place or something

def update_inv_corners(thing, piece):
    inv_corners = {v: k for k, v in thing.corners.items()}
    if piece in inv_corners:
        faces = inv_corners[piece]
    elif (piece[1], piece[2], piece[0]) in inv_corners:
        faces = inv_corners[(piece[1], piece[2], piece[0])]
    else:
        faces = inv_corners[(piece[2], piece[0], piece[1])]
    return inv_corners, faces

def white_corners(thing, solution):
    #movelist 
    moves = [thing.white0, thing.red1, thing.darkblue2, thing.yellow3, thing.purple4, thing.darkgreen5, thing.gray6, thing.orange7, thing.lightblue8, thing.cream9, thing.pink10, thing.lightgreen11]
    moveset = [6, 7, 8, 9, 10, 11]
    #check which direction white faces
    whitecorners = [(0, 3, 4), (0, 4, 5), (0, 5, 1), (0, 1, 2), (0, 2, 3)]
    aboveslots = [(3, 7, 4), (4, 8, 5), (5, 9, 1), (1, 10, 2), (2, 11, 3)]
    #slots order (from perspective of white): R U L
    #moves according to aboveslots: R U F

    for i in range(0, 5): #looping through all five corners
        piece = whitecorners[i]
        
        #check if solved
        if thing.corners[whitecorners[i]] == whitecorners[i]:
            continue

        
        right = moves[aboveslots[i][0]]        
        up = moves[aboveslots[i][1]]
        
        #check if corner is already in slot 
        faces = update_inv_corners(thing, piece)[1]
        # print(faces)

        if faces in whitecorners:       #take out corner     these are not the right moves... which slot it is in and use those as r and u
            idx = whitecorners.index(faces)
            right1 = moves[aboveslots[idx][0]]
            up1 = moves[aboveslots[idx][1]]
            right1(1)
            solution.append((right1.__name__, 1))
            up1(1)
            solution.append((up1.__name__, 1))
            right1(-1)
            solution.append((right1.__name__, -1))

        # print(solution)
        #move pieces to correct aboveslot
        corner_moves = move_corner(thing, piece, aboveslots[i], moveset, 8)
        for m in corner_moves:
            solution.append((m.__name__, 1))

        #check white direction and insert accordingly
        cornerstate = thing.corners[aboveslots[i]]
        


        if cornerstate[0] == 0: #white faces right
            right(1)
            solution.append((right.__name__, 1))
            up(1)
            solution.append((up.__name__, 1))
            right(-1)
            solution.append((right.__name__, -1))
            continue

        elif cornerstate[1] == 0:  #white faces up
            right(1)
            solution.append((right.__name__, 1))
            up(2)
            solution.append((up.__name__, 2))
            right(-1)
            solution.append((right.__name__, -1))
            up(-1)
            solution.append((right.__name__, -1))
            right(1)
            solution.append((right.__name__, 1))
            up(1)
            solution.append((up.__name__, 1))
            right(-1)
            solution.append((right.__name__, -1))
            continue

        else: #white faces left     U R U' R'
            up(1)
            solution.append((up.__name__, 1))
            right(1)
            solution.append((right.__name__, 1))
            up(-1)
            solution.append((up.__name__, -1))
            right(-1)
            solution.append((right.__name__, -1))
            continue

    return solution



