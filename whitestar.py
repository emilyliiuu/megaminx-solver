from minx import Minx

solution = []

'''
around 15 moves for cross

cases
0. cross is solved but not aligned. check which rotation of white face is most optimal with the maximum matched edges
   should eventually change this to check what the optional rotation is for the white face before solving
1. if non-white edge is matched on a white-adjacent face, rotate until white edge matches
2. if non white edge is "matched" on a white-adjacent face (different color), calculate rotations for white face, do case
    1, then rotate back to original position 
3. if white edge is matched but non white edge is not matched, take corner out (rotate face it is on once), do case 2
4. if white edge is not on an a white-adjacent face, rotate face that the edge is on until the edge is on a white-adjacent 
   face, then do case 2
5. if white edge is facing wrong way on white face, take corner out (rotate face it is on once), do case 2 on adjacent face

'''
def update_inv_edges(thing, i):
        idx = 0
        inv_edges = {v: k for k, v in thing.edges.items()}
        print(inv_edges) 
        if (0, i) in inv_edges: #finding where white-color edge is 
           # print("updating inv edges")
            #print(i)
            faces = inv_edges[(0, i)]
            # print(faces)
            idx = 1
        else:
            faces = inv_edges[(i, 0)]
        return inv_edges, faces, idx

def direction(thing, faces):
    direction = -1 if faces[1] > 6 or faces[0] >6  else 1 
    return direction



def white_star(thing):
    moves = [thing.white0, thing.red1, thing.darkblue2, thing.yellow3, thing.purple4, thing.darkgreen5, thing.gray6, thing.orange7, thing.lightblue8, thing.cream9, thing.pink10, thing.lightgreen11]
    inv_edges = {v: k for k, v in thing.edges.items()}
    
    def case1(thing, faces, i, currface=999): #faces[0] is always 0 (white)
        white_adj = [4, 5, 1, 2, 3]
        print("enter case 1")
        if currface==999:
            currface = i
        moves = [thing.white0, thing.red1, thing.darkblue2, thing.yellow3, thing.purple4, thing.darkgreen5, thing.gray6, thing.orange7, thing.lightblue8, thing.cream9, thing.pink10, thing.lightgreen11]
        dirc = direction(thing, faces)
        # print(faces)
        count = 0
        while faces[0]!= 0:
            if (faces[1] not in white_adj) and (faces[0] not in white_adj):
                print(faces[1])
                print(faces[0])
                print(white_adj)
                raise Exception("piece is not on white adjacent and should not be in case 1")
            print("first loop is broken")
            move = moves[currface]
            move(dirc) 
            solution.append((move.__name__, dirc))
            inv_edges, faces, idx = update_inv_edges(thing, i)
            print(solution)

        # if currface != 999:
        #     move(-dirc)
        #     solution.append((move.__name__, -1*dirc))
        inv_edges, faces, idx = update_inv_edges(thing, i)
        print(solution)
        return inv_edges
            

    def case2(thing, faces, i): 
    #calculate rotations for white face, then do case 1, then rotate back to original position
    #difference between i and faces is num rotations for white face
        print("enter case 2")
        moves = [thing.white0, thing.red1, thing.darkblue2, thing.yellow3, thing.purple4, thing.darkgreen5, thing.gray6, thing.orange7, thing.lightblue8, thing.cream9, thing.pink10, thing.lightgreen11] 
        idx = 0 if thing.edges[faces][1]==0 else 1
        undomove = 0
        # print(faces)
        print(idx)
        currface = faces[idx] #face that the non white color is currently on
        if currface not in white_adj:
            currface = faces[idx^1] #i think this breaks things
            # undomove = 1
            # move = moves[currface]
            # count = 0
            # while faces[idx] not in white_adj:
            #     print("new loop")
            #     # raise Exception("bruuuhhh")
            #     move(1)
            #     solution.append((move.__name__, 1))
            #     count+=1
            #     inv_edges, faces, idx = update_inv_edges(thing, i)

        rotations = i-currface if i>currface else -(currface-i)

        thing.white0(rotations)
        inv_edges, faces, idx = update_inv_edges(thing, i)
        if rotations != 0:
            solution.append((thing.white0.__name__, rotations))
        thing.print_state()

        inv_edges = case1(thing, faces, i, currface) 
        thing.white0(-rotations)
        inv_edges, faces, idx = update_inv_edges(thing, i)
        if rotations != 0:
            solution.append((thing.white0.__name__, -rotations))
        # if undomove == 1:
        #     # raise Exception("lol hi")
        #     move(-1*count)
        #     solution.append((move.__name__, -1*count))
        print(solution)
        return inv_edges

    white_adj = [4, 5, 1, 2, 3]
    state = thing.state

    #checking optimal rotation of white face
    if state[0][1]==0 and state[0][3]==0 and state[0][5]==0 and state[0][7]==0 and state[0][9]==0: #IF ALL ARE WHITE EDGES AND ARE MATCHED TO THE WHITE CENTER, ROTATE 5 TIMES AND SEE WHAT THE MAXIMUM MATCHED EDGES IS. IF IT GOES ABOVE 3, ALL EDGES ARE MATCHED.
        print("checking max matches")
        thing.print_state()
        maxmatches = 0
        bestrotations = 0
        for i in range(5): #loop through 5 rotations
            count = 0
            for j in range(5): #check each edge to see if they match
                if list(thing.edges.values())[j][1] == white_adj[j]:  # cannot access value in dictionary by index
                    count+=1
            if count>maxmatches:
                maxmatches = count
                bestrotations = i
            thing.white0(1)
        thing.white0(bestrotations)
        inv_edges, faces, idx = update_inv_edges(thing, i)
        thing.print_state()
        solution.append((thing.white0.__name__, bestrotations))

    #red darkblue yellow purple darkgreen
    for i in range(1, 6):     #looping 5 times for each face on white star
        inv_edges, faces, idx = update_inv_edges(thing, i)
        print("this is i: ")
        print(i)
        idx = 0 #nonwhite idx in faces
        #find edge piece in relation to two faces
        if (0, i) in inv_edges:
            faces = inv_edges[(0, i)]
            idx = 1
        else:
            faces = inv_edges[(i, 0)]

        #check if solved
        #cannot use faces alone to check if it is solved
        gotocase5 = False
        #if thing.edges[faces] == (0, i):
        if faces == (0, i):
            # print("checking if edges are correct")
            # print(faces)
            print(thing.edges[faces])
            if thing.edges[faces] == (i, 0):
                print("flipped edge detected")
                gotocase5 = True
            if not gotocase5:
                print("edge is solved")
                print(i)
                continue
        
        # print(faces[idx])
        print(white_adj)
        #case 1: non-white edge matched on a white-adjacent face
        if faces[idx] == i : 
            print("here1")
            print("enter case 1")
            # print(faces)
            inv_edges = case1(thing, faces, i, i)
            continue 
        
        
        #case 2: non-white edge is "matched" on a white adjaacent face (different color)
        elif faces[idx] in white_adj and faces[idx^1]!=0:
            print("here2")
            inv_edges = case2(thing, faces, i)
            continue

        #case 3: white edge is matched but non-white edge is not matched
        elif faces[idx^1] == 0:
            print("here3")
            move = moves[faces[1]]
            move(1)
            inv_edges, faces, idx = update_inv_edges(thing, i)
            solution.append((move.__name__, 1))
            case2(thing, faces, i)
            continue
        #case 3.5:white edge is on a white-adjacent face
        elif(faces[0] in white_adj) or (faces[1] in white_adj):
            print("here3.5")
            #rotate white adj face that white is on until color edge is on white adj face
            idx = 1 if thing.edges[faces][1]==0 else 0
            move = moves[faces[idx]]
            while(faces[idx^1] not in white_adj):
                move(1)
                solution.append((move.__name__, 1))
                print(solution)
                inv_edges, faces, idx = update_inv_edges(thing, i)
            # print(faces)
            case2(thing, faces, i)
        #case 4: white edge is not on an white-adjacent face
        elif (faces[0] not in white_adj) and (faces[1] not in white_adj):
            print("here4")
            #rotate face that edge is on (non gray) onto a white adjacent face, do case 2
            idx = 1 if thing.edges[faces][1]==0 else 0
            move = moves[faces[idx]]
            if faces[idx] == 6:
                move = moves[faces[idx^1]]
            #count = 0
            while (faces[0] not in white_adj) and (faces[1] not in white_adj): 
                print("this loop is broken")        #broken on gray face
                move(1)
                solution.append((move.__name__, 1))
                print(solution)
                #count +=1
                inv_edges, faces, idx = update_inv_edges(thing, i)
            #solution.append((move.__name__, count))
            case2(thing, faces, i)
            continue
        else:
            print("in case 5\n\n\n\n\n")
            # print(faces)
            print(i)
            move = moves[faces[1]]
            solution.append((move.__name__, 1))
            move(1)
            inv_edges, faces, idx = update_inv_edges(thing, i)
            case2(thing, faces, i)

        print("piece " + str(i) + " is solved\n\n\n")
        
        

        

    
    return solution
      
          
      
