from minx import Minx

'''
PLAN:
move edge piece to right spot (match one color of edge to center piece) using casework
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

def secondhalfedges(thing, solution):
    moves = [thing.white0, thing.red1, thing.darkblue2, thing.yellow3, thing.purple4, thing.darkgreen5, thing.gray6, thing.orange7, thing.lightblue8, thing.cream9, thing.pink10, thing.lightgreen11]
    layeredges = [(11, 7), (7, 8), (8, 9), (9, 10), (10, 11)]
    insertpositions = [(6, 11), (6, 7), (6, 8), (6, 9), (6, 10)] #insert left positions


    
    moveset = [(6, 7, 11), (6, 8, 7), (6, 9, 8), (6, 10, 9), (6, 11, 10)]



    for i in range(0, 5):   #loop through all 5 edges
        piece = layeredges[i]
        #check if solved
        if thing.edges[layeredges[i]] == layeredges[i]:
            continue

        #check if piece is in slot
        faces = update_inv_edges(thing, piece)[1]
        if faces in layeredges:     #take out corner            find which slot it is in and use its moveset 
            idx = layeredges.index(faces)
            right1 = moves[moveset[idx][2]]
            up1 = thing.gray6
            front1 = moves[moveset[idx][1]]
            
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

        while faces != insertpositions[i]:   #move to correct slot
            thing.gray6(1)
            solution.append((thing.gray6.__name__, 1))
            faces = update_inv_edges(thing, piece)[1]

        if thing.edges[faces] == piece:
            insertleft = 0
        else:
            insertleft = 1


        if insertleft:    
            left = moves[moveset[i][1]]
            up = moves[moveset[i][0]]
            front = moves[moveset[i][2]]

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
            continue

        else:  
            right = moves[moveset[i][2]]
            up = moves[moveset[i][0]]
            front = moves[moveset[i][1]]
            
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
            continue

    return solution




