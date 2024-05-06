from minx import Minx


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

def update_inv_corners(thing, piece):
    inv_corners = {v: k for k, v in thing.corners.items()}
    if piece in inv_corners:
        faces = inv_corners[piece]
    elif (piece[1], piece[2], piece[0]) in inv_corners:
        faces = inv_corners[(piece[1], piece[2], piece[0])]
    else:
        faces = inv_corners[(piece[2], piece[0], piece[1])]
    return inv_corners, faces


def secondhalfcorners(thing, solution):
    #movelist 
    moves = [thing.white0, thing.red1, thing.darkblue2, thing.yellow3, thing.purple4, thing.darkgreen5, thing.gray6, thing.orange7, thing.lightblue8, thing.cream9, thing.pink10, thing.lightgreen11]

    #check which direction white faces
    corners = [(10, 11, 2), (9, 10, 1), (8, 9, 5), (7, 8, 4), (11, 7, 3)]
    aboveslots = [(6, 11, 10), (6, 10, 9), (6, 9, 8), (6, 8, 7), (6, 7, 11)]
    #moves according to aboveslots: R U F

    for i in range(0, 5): #looping through all five corners
        piece = corners[i]

        right = moves[aboveslots[i][2]]
        up = moves[aboveslots[i][0]]
        
        #check if solved
        if thing.corners[corners[i]] == corners[i]:
            continue
        
        faces = update_inv_corners(thing, piece)[1]
        if faces in corners:       #take out corner   
            idx = corners.index(faces)
            right1 = moves[aboveslots[idx][2]]
            up1 = thing.gray6
            right1(1)
            solution.append((right1.__name__, 1))
            up1(1)
            solution.append((up1.__name__, 1))
            right1(-1)
            solution.append((right1.__name__, -1))

        while faces != aboveslots[i]:   #move to correct slot
            thing.gray6(1)
            solution.append((thing.gray6.__name__, 1))
            faces = update_inv_corners(thing, piece)[1]

        #check white direction and insert accordingly
        cornerstate = thing.corners[aboveslots[i]]

        if cornerstate[2] == piece[2]: #bottom color faces right
            right(1)
            solution.append((right.__name__, 1))
            up(1)
            solution.append((up.__name__, 1))
            right(-1)
            solution.append((right.__name__, -1))
            continue

        elif cornerstate[0] == piece[2]:  #white faces up
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



