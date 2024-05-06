from minx import Minx
from randommoves import move_edge

'''
PLAN:
move edge piece to right spot (match one color of edge to center piece) using bfs probably
depending on which color is touching, need to rotate the edge either LEFT or RIGHT into slot
1. insert LEFT
2. insert RIGHT

todo:
find out how to move edges to right place
check which direction to rotate
algorithms to insert:
1. U' L' U L U F U' F'
2. U R U' R' U' F' U F
loop through all 5 edges

'''

solution = []

def update_inv_edges(thing, piece):
        inv_edges = {v: k for k, v in thing.edges.items()}
        if piece in inv_edges: 
            faces = inv_edges[piece]
        else:
            faces = inv_edges[(piece[1], piece[0])]
        return inv_edges, faces

def firstlayeredges(thing, solution):
    moves = [thing.white0, thing.red1, thing.darkblue2, thing.yellow3, thing.purple4, thing.darkgreen5, thing.gray6, thing.orange7, thing.lightblue8, thing.cream9, thing.pink10, thing.lightgreen11]
    moveset_random = [6, 7, 8, 9, 10, 11]
    layeredges = [(3, 4), (4, 5), (5, 1), (1, 2), (2, 3)]
    insertpositions = [(3, 7), (4, 8), (5, 9), (1, 10), (2, 11)] #always in insert left position


    
    moveset = [(3, 7, 4), (4, 8, 5), (5, 9, 1), (1, 10, 2), (2, 11, 3)]



    for i in range(0, 5):   #loop through all 5 edges
        piece = layeredges[i]
        #check if solved
        if thing.edges[layeredges[i]] == layeredges[i]:
            # print("edge is solved")
            continue
        
        #check if piece is in slot
        faces = update_inv_edges(thing, piece)[1]
        # print(faces)
        if faces in layeredges:     #take out edge            find which slot it is in and use its moveset 
            idx = layeredges.index(faces)
            right1 = moves[moveset[idx][0]]
            up1 = moves[moveset[idx][1]] 
            front1 = moves[moveset[idx][2]]
            
            up1(1)
            solution.append((up1.__name__, 1))
            right1(1)
            solution.append((right1.__name__, 1))
            up1(-1)
            solution.append((up1.__name__, -1))
            right1(-1)
            solution.append((right1.__name__, -1))
            up1(-1)
            solution.append((up1.__name__, -1))
            front1(-1)
            solution.append((front1.__name__, -1))
            up1(1)
            solution.append((up1.__name__, 1))
            front1(1)
            solution.append((front1.__name__, 1))

        faces = update_inv_edges(thing, piece)[1]
        # print(faces)
        #move piece to insert position
        moves_used = move_edge(thing, piece, insertpositions[i], moveset_random, 8)
        for m in moves_used:
            solution.append((m.__name__, 1))

        #determine rotate left or right 
        # if thing.edges[insertpositions[i]][0] == layeredges[0]:
        faces = update_inv_edges(thing, piece)[1]
        # print(faces)
        # print(piece)
        
        if thing.edges[faces] == piece:
            insertleft = 1
            print("inserting left")
        else:
            print("inserting right")
            insertleft = 0


        if insertleft:    
            left = moves[moveset[i][2]]
            up = moves[moveset[i][1]]
            front = moves[moveset[i][0]]

            up(-1)
            solution.append((up.__name__, -1))
            left(-1)
            solution.append((left.__name__, -1))
            up(1)
            solution.append((up.__name__, 1))
            left(1)
            solution.append((left.__name__, 1))
            up(1)
            solution.append((up.__name__, 1))
            front(1)
            solution.append((front.__name__, 1))
            up(-1)
            solution.append((up.__name__, -1))
            front(-1)
            solution.append((front.__name__, -1))
            faces = update_inv_edges(thing, piece)[1]

            # print(faces)
            continue

        else:  
            right = moves[moveset[i][0]]
            up = moves[moveset[i][1]]
            front = moves[moveset[i][2]]

            up(1) #setup move
            solution.append((up.__name__, 1))

            up(1)
            solution.append((up.__name__, 1))
            right(1)
            solution.append((right.__name__, 1))
            up(-1)
            solution.append((up.__name__, -1))
            right(-1)
            solution.append((right.__name__, -1))
            up(-1)
            solution.append((up.__name__, -1))
            front(-1)
            solution.append((front.__name__, -1))
            up(1)
            solution.append((up.__name__, 1))
            front(1)
            solution.append((front.__name__, 1))
            faces = update_inv_edges(thing, piece)[1]

            # print(faces)
            continue

    return solution




