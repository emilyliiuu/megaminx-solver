from minx import Minx
import math

'''
corners:
- check corner is on top face 
- if not on top face:
	- if in non-corner slot (middle slot)
		- r u r' with corner in far right
	- if in corner slot 
		- f2
- if on top face
	- rotate gray until corner is in top right corner above correct slot
- repeat sexy move until front face of corner matches front face color
	- corner can either be in top right or bottom right slot?
- f2 or f into correct slot

edges:
- fixed front (this might be a lie)
- find location of edge piece
- if not on top face
	- if in middle slot
		- rotate either face it is on, u, undo first move
	- if in bottom slot
		- check which slot it is in, f if in left slot, f' if in right slot
		- if left, do left edge inserting alg
		- if right, do right edge inserting alg
		- undo first move
- if on top face
	- rotate edge piece to above slot
- if edge matches front face
	- u
	- if insert left, f (first move)
	- if insert right, f' (first move)
	- u'
	- do left/right inserting alg
	- undo first move 
- if edge does not match front face
	- if insert left, u f (first move)
	- if insert right, u' f' (first move)
	- use left slot corner as ruf (left) USING RIGHT INSERTING ALG, use right slot corner as luf (right) USING LEFT INSERTING ALG
	- undo first move

'''

solution = []
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

def insert_corners(thing, solution):
    #movelist 
    moves = [thing.white0, thing.red1, thing.darkblue2, thing.yellow3, thing.purple4, thing.darkgreen5, thing.gray6, thing.orange7, thing.lightblue8, thing.cream9, thing.pink10, thing.lightgreen11]

    cornerstoinsert = [(3, 7, 4), (4, 8, 5), (5, 9, 1), (1, 10, 2), (2, 11, 3)]
    aboveslots = [(6, 7, 11), (6, 8, 7), (6, 9, 8), (6, 10, 9), (6, 11, 10)]
    middleslots = [(11, 7, 3), (7, 8, 4), (8, 9, 5), (9, 10, 1), (10, 11, 2)]


    for i in range(0, 5): #looping through all five corners
        piece = cornerstoinsert[i]
        right = moves[aboveslots[i][2]]
        up = moves[aboveslots[i][0]]
        front = moves[aboveslots[i][1]]
        
        #check if solved
        if thing.corners[cornerstoinsert[i]] == cornerstoinsert[i]: #THIS DOES NOT CHECK IF IT IS ROTATED!!!!! NEED TO CHECK IF ACTUALLY SOLVED!!!!!
            print("corner solved")
            continue
        
        faces = update_inv_corners(thing, piece)[1]
        #check if on top face
        topface = False
        if faces[0] == 6:
            topface = True

        #not on top face -> need to move to top face
        if not topface:
            if faces in middleslots:
                print("corner in middle slot")
                right1 = moves[faces[0]] #different moves from before
                # print(right1.__name__)
                right1(1)
                solution.append((right1.__name__, 1))
                up(1)
                # print(up.__name__)
                solution.append((up.__name__, 1))
                right1(-1)
                # print(right1.__name__)
                faces = update_inv_corners(thing, piece)[1]
                # print(faces)
                solution.append((right1.__name__, -1))

            elif faces in cornerstoinsert:
                front1 = moves[faces[1]] #idk
                front1(2)
                solution.append((front1.__name__, 2))

        faces = update_inv_corners(thing, piece)[1]
        
        #now piece is on top face, move to correct aboveslot
        while faces != aboveslots[i]:
            # print(faces)
            print("stuck in up")
            up(1)
            solution.append((up.__name__, 1))
            faces = update_inv_corners(thing, piece)[1]

        # print(piece)
        # print(faces)
        correctposition = 1
        #piece is in slot, repeat sexy until front face of corner matches face color
        while (thing.state[i+7][0] != cornerstoinsert[i][1]) or not correctposition:  #changed from i+7
            
            print("sexY")
            right(1)
            solution.append((right.__name__, 1))
            up(1)
            solution.append((up.__name__, 1))
            right(-1)
            solution.append((right.__name__, -1))
            up(-1)
            solution.append((up.__name__, -1))
            if thing.corners[aboveslots[i]] != piece:
                correctposition = 0
            else:
                correctposition = 1
            print(i+7)
            print(thing.state[i+7][0])
        
        faces = update_inv_corners(thing, piece)[1]
        # print(faces)
        # print("\n")
        

        #move into slot
        front(2)
        solution.append((front.__name__, 2))
        faces = update_inv_corners(thing, piece)[1]
        # print(faces)
        # print("\n")
        print("\n\n\n\n")
        print(piece)
        print(thing.corners[piece])
        

    return solution


def insert_edges(thing, solution):
    #movelist 
    moves = [thing.white0, thing.red1, thing.darkblue2, thing.yellow3, thing.purple4, thing.darkgreen5, thing.gray6, thing.orange7, thing.lightblue8, thing.cream9, thing.pink10, thing.lightgreen11]

    #check which direction white faces
    edgestoinsert = [(3, 7), (4, 7), (4, 8), (5, 8), (5, 9), (1, 9), (1, 10), (2, 10), (2, 11), (3, 11)]
    #if idx%2 is 0, right slot, otherwise left slot
    aboveslots = [(6, 7), (6, 8), (6, 9), (6, 10), (6, 11)]
    middleslots = [(11, 7), (7, 8), (8, 9), (9, 10), (10, 11)]
    moveset = [(11, 7, 3), (7, 8, 4), (7, 8, 4), (8, 9, 5), (8, 9, 5), (9, 10, 1), (9, 10, 1), (10, 11, 2), (10, 11, 2), (11, 7, 3)] 

    for i in range (0, 10):
        print(i)
        piece = edgestoinsert[i]
        print(piece)
        faces = update_inv_edges(thing, piece)[1]

        up = moves[6]
        

        #check if solved
        if thing.edges[edgestoinsert[i]] == edgestoinsert[i]:     #DOESNT CHECK IF EDGE IS FLIPPED!!!!! actually i think it does

            continue

        #check if on top face
        topface = False
        if faces[0] == 6:
            topface == True
    
        #if not on top face
        if not topface:
            print("not on top face")
            print(faces) #gets stuck when cross is wrong. fix cross and this should be good
            if (faces in middleslots) or ((faces[1], faces[0]) in middleslots):
                print("piece in middleslots")
                move = moves[faces[0]]
                move(1)
                solution.append((move.__name__, 1))
                up(1)
                solution.append((up.__name__, 1))
                move(-1)
                solution.append((move.__name__, -1))
            elif (faces in edgestoinsert) or ((faces[1], faces[0]) in edgestoinsert):
                print("piece in edge slot")
                idx = edgestoinsert.index(faces)
                #need to change moveset here
                if idx%2==0:
                    print("piece in right insert slot")
                    front = moves[moveset[idx][1]]
                    right = moves[moveset[idx][0]]

                    front(-1)
                    solution.append((front.__name__, -1))
                    #take out edge using right insert
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

                    #undo first move
                    front(1)
                    solution.append((front.__name__, 1))
                else:
                    print("piece in left insert slot")
                    front = moves[moveset[idx][0]]
                    left = moves[moveset[idx][1]]
                    front(1)
                    solution.append((front.__name__, 1))
                    #take out edge using left insert
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

                    #undo first move
                    front(-1)
                    solution.append((front.__name__, -1))

        inv_edges, faces = update_inv_edges(thing, piece)
        # print(solution)
        # print(faces)
        # thing.print_state()
        #print(inv_edges)
        #now on top face, move to correct above slot
        slotidx = math.floor(i/2)
        while (faces != aboveslots[slotidx]) and ((faces[1], faces[0]) != aboveslots[slotidx]):
            # print(faces)
            # print(aboveslots[slotidx])
            # print("rotating to move to correct slot")
            up(1)
            solution.append((up.__name__, 1))
            faces = update_inv_edges(thing, piece)[1]
        
        print(faces)
        # print(faces)
        #if edge matches front face
        if thing.edges[faces][1] == math.floor(i/2)+7:  #this is kinda sussy
            print(faces[1])
            print(math.floor(i/2)+7)
            print("edge matches front face")
            if i%2==0: 
                print("insert right")
                front = moves[moveset[i][1]]
                right = moves[moveset[i][0]]
                #insert right setup
                up(1)
                solution.append((up.__name__, 1))
                front(-1)
                solution.append((front.__name__, -1))
                up(-1)
                solution.append((up.__name__, -1))

                #right insert
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

                front(1)
                solution.append((front.__name__, 1))

                faces = update_inv_edges(thing, piece)[1]
                print(faces)
                continue 
            else:
                print("insert left")
                front = moves[moveset[i][0]]
                left = moves[moveset[i][1]]
                #insert left setup
                up(1)
                solution.append((up.__name__, 1))
                front(1)
                solution.append((front.__name__, 1))
                up(-1)
                solution.append((up.__name__, -1))

                #left insert
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

                front (-1)
                solution.append((front.__name__, -1))

                faces = update_inv_edges(thing, piece)[1]
                print(faces)
                continue

        #edge does not match front face
        else:
            print("edge does not match front face")
            if i%2 == 0: #insert right
                print("insert right")
                
                # up(-1)
                # solution.append((up.__name__, 1))
                # front(-1)
                # solution.append((front.__name__, -1))

                left1 = moves[moveset[i][1]] #use moveset
                front1 = moves[moveset[i][0]] #this is wrong

                #setup moves 
                up(-1)
                solution.append((up.__name__, -1))
                left1(-1)
                solution.append((left1.__name__, -1))
                #INSERT USING LEFT INSERT ALG
                up(-1)
                solution.append((up.__name__, -1))
                left1(-1)
                solution.append((left1.__name__, -1))
                up(1)
                solution.append((up.__name__, 1))
                left1(1)
                solution.append((left1.__name__, 1))
                up(1)
                solution.append((up.__name__, 1))
                front1(1)
                solution.append((front1.__name__, 1))
                up(-1)
                solution.append((up.__name__, -1))
                front1(-1)
                solution.append((front1.__name__, -1))

                left1(1)
                solution.append((left1.__name__, 1))

                faces = update_inv_edges(thing, piece)[1]
                print(faces)
                continue

            else: #insert left
                print("insert left")
                
                # up(1)
                # solution.append((up.__name__, -1))
                # front(1)
                # solution.append((front.__name__, 1))

                right1 = moves[moveset[i][0]] 
                front1 = moves[moveset[i][1]]

                #setup moves
                up(1)
                solution.append((up.__name__, 1))
                right1(1)
                solution.append((right1.__name__, 1))

                #INSERT USING RIGHT INSERT ALG
                up(1)
                solution.append((up.__name__, 1))
                right1(1)
                solution.append((right1.__name__, 1))
                up(-1)
                solution.append((up.__name__, -1))
                right1(-1)
                solution.append((right1.__name__, -1))
                up(-1)
                solution.append((up.__name__, -1))
                front1(-1)
                solution.append((front1.__name__, -1))
                up(1)
                solution.append((up.__name__, 1))
                front1(1)
                solution.append((front1.__name__, 1))

                right1(-1)
                solution.append((right1.__name__, -1))

                faces = update_inv_edges(thing, piece)[1]
                print(faces)
                continue




            

            
    return solution