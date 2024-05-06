from minx import Minx
import random
#works for moving an edge piece to a target slot.

def update_inv_edges(thing, piece):
        inv_edges = {v: k for k, v in thing.edges.items()}
        if piece in inv_edges: 
            faces = inv_edges[piece]
        else:
            faces = inv_edges[(piece[1], piece[0])]
        return inv_edges, faces

def update_inv_corners(thing, piece):
    inv_corners = {v: k for k, v in thing.corners.items()}
    if piece in inv_corners:
        faces = inv_corners[piece]
    elif (piece[1], piece[2], piece[0]) in inv_corners:
        faces = inv_corners[(piece[1], piece[2], piece[0])]
    else:
        faces = inv_corners[(piece[2], piece[0], piece[1])]
    return inv_corners, faces

def move_edge(thing, piece, target, moveset, max_moves):
    moves = [thing.white0, thing.red1, thing.darkblue2, thing.yellow3, thing.purple4, thing.darkgreen5, thing.gray6, thing.orange7, thing.lightblue8, thing.cream9, thing.pink10, thing.lightgreen11] 
    for attempt in range(5000):
        #thing.print_state()
        moves_used = []

        faces = update_inv_edges(thing, piece)[1]

        for i in range(max_moves+1):
            if faces == target:
                #return "Target position reached in {} moves: {}".format(len(moves_used), moves_used)
                return moves_used

            moveidx = random.choice(faces)
            #print(faces)
            #print(moveidx)
            if moveidx in moveset:
                #print('moveidx is in moveset')
                move = moves[moveidx]
                move(1)
                faces = update_inv_edges(thing, piece)[1]
                moves_used.append(move)
            else:
                i-=1
                continue
        reset_puzzle(thing, moves_used)
        #print("Attempt {} failed. Resetting puzzle and trying again.".format(attempt + 1))

    return "Maximum number of attempts reached. Target position not reached."

def move_corner(thing, piece, target, moveset, max_moves):
    moves = [thing.white0, thing.red1, thing.darkblue2, thing.yellow3, thing.purple4, thing.darkgreen5, thing.gray6, thing.orange7, thing.lightblue8, thing.cream9, thing.pink10, thing.lightgreen11] 
    for attempt in range(1000):
        #thing.print_state()
        moves_used = []

        faces = update_inv_corners(thing, piece)[1]
        #print(faces)

        for i in range(max_moves+1):
            if faces == target:
                moves_names = []
                for m in moves_used:
                    moves_names.append((m.__name__, 1))
                #return "Target position reached in {} moves: {}".format(len(moves_used), moves_names)
                return moves_used

            moveidx = random.choice(faces)
            #print(moveidx)
            if moveidx in moveset:
                move = moves[moveidx]
                move(1)
                faces = update_inv_corners(thing, piece)[1]
                moves_used.append(move)
            else:
                i-=1
                continue
        reset_puzzle(thing, moves_used)
        #print("Attempt {} failed. Resetting puzzle and trying again.".format(attempt + 1))

    return "Maximum number of attempts reached. Target position not reached."
    

def reset_puzzle(thing, moves_used):
    moves_used.reverse()
    for move in moves_used:
        move(-1)