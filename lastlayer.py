from minx import Minx
import copy

'''
4 phases
1. edge orientation
2. corner orientation
3. edge permutation
4. corner permutation

EDGE ORIENTATION
-   read edge pieces in a circle, rotate until recognized in one of three edge 
    orientation cases
-   do algorithm

CORNER ORIENTATION
-   read around gray face, rotate until recognized in one of 16 corner orientation cases
-   do algorithm

EDGE PERMUTATION
-   NO CLUE FIGURE THIS OUT LATER

CORNER PERMUTATION
-   im going to throw something across the room
'''

def lastlayer(thing, solution):

    moves = [thing.white0, thing.red1, thing.darkblue2, thing.yellow3, thing.purple4, thing.darkgreen5, thing.gray6, thing.orange7, thing.lightblue8, thing.cream9, thing.pink10, thing.lightgreen11]

    #EDGE ORIENTATION 
    ############ FIND OUT WHERE TO DEAL WITH EDGE ORIENTATION ALREADY SOLVED
    print("DOING EDGE ORIENTATION")
    moveset = (6, 9, 10)
    right = moves[moveset[1]]
    front = moves[moveset[2]]
    up = moves[moveset[0]]
    edgecases=[(0, 1, 1, 0, 1), (0, 1, 1, 1, 0), (0, 1, 0, 0, 0)]
    edgestate = (thing.state[6][1]==6, thing.state[6][9]==6, thing.state[6][7]==6, thing.state[6][5]==6, thing.state[6][3]==6)
    for i in range(5):
        case = 0
        edgestate = (thing.state[6][1]==6, thing.state[6][9]==6, thing.state[6][7]==6, thing.state[6][5]==6, thing.state[6][3]==6)
        if edgestate == edgecases[0]:
            case = 1
            break
        elif edgestate == edgecases[1]:
            case = 2
            break
        elif edgestate == edgecases[2]:
            case = 3
            break
        thing.gray6(1)
        solution.append((moves[6].__name__, 1))

    if case == 1:
        front(1)
        solution.append((front.__name__, 1))
        right(1)
        solution.append((right.__name__, 1))
        up(1)
        solution.append((up.__name__, 1))
        right(-1)
        solution.append((right.__name__, -1))
        up(-1)
        solution.append((up.__name__, -1))
        front(-1)
        solution.append((front.__name__, -1))
    
    elif case == 2:
        front(1)
        solution.append((front.__name__, 1))
        up(1)
        solution.append((up.__name__, 1))
        right(1)
        solution.append((right.__name__, 1))
        up(-1)
        solution.append((up.__name__, -1))
        right(-1)
        solution.append((right.__name__, -1))
        front(-1)
        solution.append((front.__name__, -1))
    
    elif case == 3:
        front(1)
        solution.append((front.__name__, 1))
        right(1)
        solution.append((right.__name__, 1))
        up(2)
        solution.append((up.__name__, 2))
        right(-2)
        solution.append((right.__name__, -2))
        front(1)
        solution.append((front.__name__, 1))
        right(1)
        solution.append((right.__name__, 1))
        front(-1)
        solution.append((front.__name__, -1))
        up(-2)
        solution.append((up.__name__, -2))
        front(-1)
        solution.append((front.__name__, -1))

    else:
        print("edge orientation is solved")

    # print(solution)
    
    #CORNER ORIENTATION
    #moveset is same as edge orientation
    print("DOING CORNER ORIENTATION")
    cornercases = [(1, 1, 0, 0, 0, 0, 0, 0, 0, 0), #1 gray, 0 not gray starting from right pink going clockwise 
                   (0, 0, 0, 1, 0, 0, 1, 0, 0, 0),
                   (0, 0, 0, 1, 0, 0, 0, 0, 1, 0),
                   (0, 0, 0, 0, 0, 0, 1, 0, 0, 1),
                   (1, 0, 0, 0, 0, 0, 1, 0, 1, 0),
                   (0, 1, 0, 0, 0, 0, 0, 1, 0, 1),
                   (0, 0, 0, 1, 0, 1, 0, 0, 0, 1),
                   (1, 0, 0, 0, 1, 0, 1, 0, 0, 0),
                   (1, 0, 0, 1, 0, 0, 1, 1, 0, 0),
                   (0, 0, 0, 0, 1, 1, 0, 0, 1, 1),
                   (0, 1, 0, 0, 0, 0, 1, 0, 1, 1),
                   (0, 1, 0, 0, 1, 0, 1, 0, 0, 1),
                   (1, 0, 0, 0, 1, 1, 0, 1, 0, 0),
                   (1, 0, 1, 1, 0, 0, 0, 1, 0, 0),
                   (1, 0, 1, 0, 1, 1, 0, 0, 1, 0),
                   (0, 1, 0, 1, 0, 0, 1, 1, 0, 1),
                   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)]
    cornerstate = (thing.state[10][0]==6, thing.state[10][2]==6, thing.state[11][0]==6, thing.state[11][2]==6, thing.state[7][0]==6, thing.state[7][2]==6, thing.state[8][0]==6, thing.state[8][2]==6, thing.state[9][0]==6, thing.state[9][2]==6)
    for i in range(5):
        case = 0
        cornerstate = (thing.state[10][0]==6, thing.state[10][2]==6, thing.state[11][0]==6, thing.state[11][2]==6, thing.state[7][0]==6, thing.state[7][2]==6, thing.state[8][0]==6, thing.state[8][2]==6, thing.state[9][0]==6, thing.state[9][2]==6)

        
        if cornerstate == cornercases[0]:
            case = 1
            break
        elif cornerstate == cornercases[1]:
            case = 2
            break
        elif cornerstate == cornercases[2]:
            case = 3
            break
        elif cornerstate == cornercases[3]:
            case = 4
            break
        elif cornerstate == cornercases[4]:
            case = 5
            break
        elif cornerstate == cornercases[5]:
            case = 6
            break
        elif cornerstate == cornercases[6]:
            case = 7
            break
        elif cornerstate == cornercases[7]:
            case = 8
            break
        elif cornerstate == cornercases[8]:
            case = 9
            break
        elif cornerstate == cornercases[9]:
            case = 10
            break
        elif cornerstate == cornercases[10]:
            case = 11
            break
        elif cornerstate == cornercases[11]:
            case = 12
            break
        elif cornerstate == cornercases[12]:
            case = 13
            break
        elif cornerstate == cornercases[13]:
            case = 14
            break
        elif cornerstate == cornercases[14]:
            case = 15
            break
        elif cornerstate == cornercases[15]:
            case = 16
            break
        elif cornerstate == cornercases[16]:
            case = 17
            print("corner orientation is solved")
            break
                
        thing.gray6(1)
        solution.append((moves[6].__name__, 1))
    
    if case==1:
        right(1)
        solution.append((right.__name__, 1))
        up(1)
        solution.append((up.__name__, 1))
        right(-1)
        solution.append((right.__name__, -1))
        up(1)
        solution.append((up.__name__, 1))
        right(1)
        solution.append((right.__name__, 1))
        up(1)
        solution.append((up.__name__, 1))
        right(-1)
        solution.append((right.__name__, -1)) #there were two right(-1)s?
        up(-2)
        solution.append((up.__name__, -2))
        right(1)
        solution.append((right.__name__, 1))
        up(-1)
        solution.append((up.__name__, -1))
        right(-1)
        solution.append((right.__name__, -1))

    elif case==2:
        front(1)
        solution.append((front.__name__, 1))
        right(1)
        solution.append((right.__name__, 1))
        up(2)
        solution.append((up.__name__, 2))
        right(-1)
        solution.append((right.__name__, -1))
        up(-1)
        solution.append((up.__name__, -1))
        right(1)
        solution.append((right.__name__, 1))
        up(-1)
        solution.append((up.__name__, -1))
        right(-1)
        solution.append((right.__name__, -1))
        front(-1)
        solution.append((front.__name__, -1))


    elif case==3:
        right(1)
        solution.append((right.__name__, 1))
        up(2)
        solution.append((up.__name__, 2))
        right(-1)
        solution.append((right.__name__, -1))
        up(1)
        solution.append((up.__name__, 1))
        right(1)
        solution.append((right.__name__, 1))
        up(2)
        solution.append((up.__name__, 2))
        right(-1)
        solution.append((right.__name__, -1))


    elif case==4:
        print('entering case 4')
        right(1)
        solution.append((right.__name__, 1))
        up(1)
        solution.append((up.__name__, 1))
        right(-1)
        solution.append((right.__name__, -1))
        up(-1)
        solution.append((up.__name__, -1))
        right(-1)
        solution.append((right.__name__, -1))
        front(1)
        solution.append((front.__name__, 1))
        right(1)
        solution.append((right.__name__, 1))
        up(1)
        solution.append((up.__name__, 1))
        right(1)
        solution.append((right.__name__, 1))
        up(-1)
        solution.append((up.__name__, -1))
        right(-1)
        solution.append((right.__name__, -1))
        front(-1)
        solution.append((front.__name__, -1))

    elif case==5:
        right(1)
        solution.append((right.__name__, 1))
        up(1)
        solution.append((up.__name__, 1))
        right(-1)
        solution.append((right.__name__, -1))
        up(1)
        solution.append((up.__name__, 1))
        right(1)
        solution.append((right.__name__, 1))
        up(-2)
        right(-1)
        solution.append((right.__name__, -1))


    elif case==6:
        right(-1)
        solution.append((right.__name__, -1))
        up(-1)
        solution.append((up.__name__, -1))
        right(1)
        solution.append((right.__name__, 1))
        up(-1)
        solution.append((up.__name__, -1))
        right(-1)
        solution.append((right.__name__, -1))
        up(2)
        solution.append((up.__name__, 2))
        right(1)
        solution.append((right.__name__, 1))
    
    elif case==7:
        right(1)
        solution.append((right.__name__, 1))
        up(2)
        solution.append((up.__name__, 2))
        right(-1)
        solution.append((right.__name__, -1))
        up(-1)
        solution.append((up.__name__, -1))
        right(1)
        solution.append((right.__name__, 1))
        up(-1)
        solution.append((up.__name__, -1))
        right(-1)
        solution.append((right.__name__, -1))

    elif case==8:
        right(1)
        solution.append((right.__name__, 1))
        up(1)
        solution.append((up.__name__, 1))
        right(-1)
        solution.append((right.__name__, -1))
        up(2)
        solution.append((up.__name__, 2))
        right(1)
        solution.append((right.__name__, 1))
        up(2)
        solution.append((up.__name__, 2))
        right(-1)
        solution.append((right.__name__, -1))

    elif case==9:
        right(1)
        solution.append((right.__name__, 1))
        up(2)
        solution.append((up.__name__, 2))
        right(-1)
        solution.append((right.__name__, -1))
        up(-1)
        solution.append((up.__name__, -1))
        right(1)
        solution.append((right.__name__, 1))
        up(1)
        solution.append((up.__name__, 1))
        right(-1)
        solution.append((right.__name__, -1))
        up(-1)
        solution.append((up.__name__, -1))
        right(1)
        solution.append((right.__name__, 1))
        up(-1)
        solution.append((up.__name__, -1))
        right(-1)
        solution.append((right.__name__, -1))

    elif case==10:
        right(1)
        solution.append((right.__name__, 1))
        up(1)
        solution.append((up.__name__, 1))
        right(-1)
        solution.append((right.__name__, -1))
        up(1)
        solution.append((up.__name__, 1))
        right(1)
        solution.append((right.__name__, 1))
        up(-1)
        solution.append((up.__name__, -1))
        right(-1)
        solution.append((right.__name__, -1))
        up(1)
        solution.append((up.__name__, 1))
        right(1)
        solution.append((right.__name__, 1))
        up(-2)
        solution.append((up.__name__, -2))
        right(-1)
        solution.append((right.__name__, -1))

    elif case==11:
        right(1)
        solution.append((right.__name__, 1))
        up(1)
        solution.append((up.__name__, 1))
        right(-1)
        solution.append((right.__name__, -1))
        up(1)
        solution.append((up.__name__, 1))
        right(1)
        solution.append((right.__name__, 1))
        up(1)
        solution.append((up.__name__, 1))
        right(-1)
        solution.append((right.__name__, -1))
        up(-1)
        solution.append((up.__name__, -1))
        right(1)
        solution.append((right.__name__, 1))
        up(-2)
        solution.append((up.__name__, -2))
        right(-1)
        solution.append((right.__name__, -1))
    
    elif case==12:
        right(1)
        solution.append((right.__name__, 1))
        up(2)
        solution.append((up.__name__, 2))
        right(-1)
        solution.append((right.__name__, -1))
        up(-1)
        solution.append((up.__name__, -1))
        right(1)
        solution.append((right.__name__, 1))
        up(-1)
        solution.append((up.__name__, -1))
        right(-2)
        solution.append((right.__name__, -2))
        up(-1)
        solution.append((up.__name__, -1))
        right(1)
        solution.append((right.__name__, 1))
        up(-1)
        solution.append((up.__name__, -1))
        right(-1)
        solution.append((right.__name__, -1))
        up(2)
        solution.append((up.__name__, 2))
        right(1)
        solution.append((right.__name__, 1))

    elif case==13:
        right(1)
        solution.append((right.__name__, 1))
        up(2)
        solution.append((up.__name__, 2))
        right(-1)
        solution.append((right.__name__, -1))
        up(-1)
        solution.append((up.__name__, -1))
        right(2)
        solution.append((right.__name__, 2))
        up(-1)
        solution.append((up.__name__, -2))
        right(-2)
        solution.append((right.__name__, -2))
        up(2)
        solution.append((up.__name__, 2))
        right(1)
        solution.append((right.__name__, 1))

    elif case==14:
        right(-1)
        solution.append((right.__name__, -1))
        up(-2)
        solution.append((up.__name__, -2))
        right(2)
        solution.append((right.__name__, 2))
        up(1)
        solution.append((up.__name__, 1))
        right(-2)
        solution.append((right.__name__, -2))
        up(1)
        solution.append((up.__name__, 1))
        right(2)
        solution.append((right.__name__, 2))
        up(-2)
        solution.append((up.__name__, -2))
        right(-1)
        solution.append((right.__name__, -1))

    elif case==15:
        right(1)
        solution.append((right.__name__, 1))
        up(1)
        solution.append((up.__name__, 1))
        right(-1)
        solution.append((right.__name__, -1))
        up(2)
        solution.append((up.__name__, 2))
        right(1)
        solution.append((right.__name__, 1))
        up(-2)
        solution.append((up.__name__, -2))
        right(-1)
        solution.append((right.__name__, -1))
        up(1)
        solution.append((up.__name__, 1))
        right(1)
        solution.append((right.__name__, 1))
        up(-2)
        solution.append((up.__name__, -2))
        right(-1)
        solution.append((right.__name__, -1))

    elif case==16:
        right(1)
        solution.append((right.__name__, 1))
        up(2)
        solution.append((up.__name__, 2))
        right(-1)
        solution.append((right.__name__, -1))
        up(-1)
        solution.append((up.__name__, -1))
        right(1)
        solution.append((right.__name__, 1))
        up(2)
        solution.append((up.__name__, 2))
        right(-1)
        solution.append((right.__name__, -1))
        up(-2)
        solution.append((up.__name__, -2))
        right(1)
        solution.append((right.__name__, 1))
        up(-1)
        solution.append((up.__name__, -1))
        right(-1)
        solution.append((right.__name__, -1))
    
    else:
        print("CORNER ORIENTATION CASE NOT FOUND")

    print("solution")

    #EDGE PERMUTATION
    #rotate to position with most solved edges and determine case
    #rotation cases can be repeated until all edges are solved
    print("DOING EDGE PERMUTATION")
    state = thing.state
    gray_adj = thing.adj_num[6]
    #determine max amount of edges solved
    maxmatches = 0
    bestrotations = 0
    edgestate = (state[10][1]==10, state[11][1]==11, state[7][1]==7, state[8][1]==8, state[9][1]==9) 
    for i in range(5): #loop through 5 rotations
        print(edgestate)
        count = sum(bool(x) for x in edgestate)
        
        if count>maxmatches:
            maxmatches = count
            bestrotations = i
        if edgestate == (1, 1, 1, 1, 1):
            break
        thing.gray6(1)
        edgestate = (state[10][1]==10, state[11][1]==11, state[7][1]==7, state[8][1]==8, state[9][1]==9)

    # print(maxmatches)
    # print(bestrotations)
    if bestrotations != 0:
        thing.gray6(bestrotations)
        solution.append((thing.gray6.__name__, bestrotations))
    edgestate = (state[10][1]==10, state[11][1]==11, state[7][1]==7, state[8][1]==8, state[9][1]==9)
    
    # print(edgestate)

    if maxmatches == 2:
        print("enter maxmatches 2")
        edgecases1 = [(1, 0, 0, 1, 0),
                      (0, 0, 1, 0, 1),
                      (0, 1, 0, 1, 0),
                      (1, 0, 1, 0, 0),
                      (0, 1, 0, 0, 1)]
        edgecases2 = [(1, 1, 0, 0, 0),
                      (1, 0, 0, 0, 1),
                      (0, 0, 0, 1, 1),
                      (0, 0, 1, 1, 0),
                      (0, 1, 1, 0, 0)]
        #case1: two edges across are solved (only needs RUF)
        if edgestate in edgecases1:
            print('edgecases 1')
            if edgestate == edgecases1[0]:
                print("in case 0")
                moveset = (9, 6, 10)
            elif edgestate == edgecases1[1]:
                moveset = (10, 6, 11)
            elif edgestate == edgecases1[2]: 
                moveset = (11, 6, 7)
            elif edgestate == edgecases1[3]:
                moveset = (7, 6, 8)
            else:
                moveset = (8, 6, 9)
            right = moves[moveset[0]]
            up = moves[moveset[1]]
            
            while edgestate != (1, 1, 1, 1, 1): #repeat until all edges solved (should take two times max)
                print("i hate this loop")
                print(edgestate)
                # print("looping")
                right(2)
                solution.append((right.__name__, 2))
                up(-2)
                solution.append((up.__name__, -2))
                right(-2)
                solution.append((right.__name__, -2))
                up(-1)
                solution.append((up.__name__, -1))
                right(2)
                solution.append((right.__name__, 2))
                up(-2)
                solution.append((up.__name__, -2))
                right(-2)
                solution.append((right.__name__, -2))

                maxmatches = 0
                bestrotations = 0
                edgestate = (state[10][1]==10, state[11][1]==11, state[7][1]==7, state[8][1]==8, state[9][1]==9) 
                if edgestate == (1, 1, 1, 1, 1):
                    break
                for i in range(5): #loop through 5 rotations
                    print(edgestate)
                    count = sum(bool(x) for x in edgestate)
                    
                    if count>maxmatches:
                        maxmatches = count
                        bestrotations = i
                    if edgestate == (1, 1, 1, 1, 1):
                        break
                    thing.gray6(1)
                    edgestate = (state[10][1]==10, state[11][1]==11, state[7][1]==7, state[8][1]==8, state[9][1]==9)
                thing.gray6(bestrotations)
                solution.append((thing.gray6.__name__, bestrotations))
                edgestate = (state[10][1]==10, state[11][1]==11, state[7][1]==7, state[8][1]==8, state[9][1]==9)
                print("using this edgestate")
                print(edgestate)

                if edgestate in edgecases1:
                    if edgestate == edgecases1[0]:
                        moveset = (9, 6, 10)
                    elif edgestate == edgecases1[1]:
                        moveset = (8, 6, 9)
                    elif edgestate == edgecases1[2]: 
                        moveset = (7, 6, 8)
                    elif edgestate == edgecases1[3]:
                        moveset = (11, 6, 7)
                    else:
                        moveset = (10, 6, 11)
                    right = moves[moveset[0]]
                    up = moves[moveset[1]]
                elif edgestate in edgecases2:
                    print("entering the weird thing for case 2")
                    if edgestate == edgecases2[0]:
                        print("in case 0")
                        moveset = (9, 6, 10)
                    elif edgestate == edgecases2[1]:
                        moveset = (8, 6, 9)
                    elif edgestate == edgecases2[2]: 
                        moveset = (7, 6, 8)
                    elif edgestate == edgecases2[3]:
                        moveset = (11, 6, 7)
                    else:
                        moveset = (10, 6, 11)
                    right = moves[moveset[0]]
                    up = moves[moveset[1]]
                    front = moves[moveset[2]]

                    right(1)
                    solution.append((right.__name__, 1))
                    up(1)
                    solution.append((up.__name__, 1))
                    right(-1)
                    solution.append((right.__name__, -1))
                    front(-1)
                    solution.append((front.__name__, -1))
                    right(1)
                    solution.append((right.__name__, 1))
                    up(1)
                    solution.append((up.__name__, 1))
                    right(-1)
                    solution.append((right.__name__, -1))
                    up(-1)
                    solution.append((up.__name__, -1))
                    right(-1)
                    solution.append((right.__name__, -1))
                    front(1)
                    solution.append((front.__name__, 1))
                    right(2)
                    solution.append((right.__name__, 2))
                    up(-1)
                    solution.append((up.__name__, -1))
                    right(-1)
                    solution.append((right.__name__, -1))
                    up(1) #auf
                    solution.append((up.__name__, 1))
                elif(edgestate == (1, 1, 1, 1, 1)):
                    break
                else:
                    edgecases = [(0, 1, 0, 0, 0),
                                (1, 0, 0, 0, 0),
                                (0, 0, 0, 0, 1),
                                (0, 0, 0, 1, 0),
                                (0, 0, 1, 0, 0)]
                    if edgestate in edgecases:
                        print(edgestate)
                        if edgestate == edgecases[0]:
                            print("enter case 0 ")
                            moveset = (9, 6, 10, 11)
                        elif edgestate == edgecases[1]:
                            moveset = (8, 6, 9, 10)
                        elif edgestate == edgecases[2]: 
                            moveset = (7, 6, 8, 9)
                        elif edgestate == edgecases[3]:
                            moveset = (11, 6, 7, 8)
                        else:
                            moveset = (10, 6, 11, 7)
                        right = moves[moveset[0]]
                        up = moves[moveset[1]]
                        front = moves[moveset[2]]
                        left = moves[moveset[3]]
                        
                        left(1)
                        solution.append((left.__name__, 1))
                        right(1)
                        solution.append((right.__name__, 1))
                        up(2)
                        solution.append((up.__name__, 2))
                        left(-1)
                        solution.append((left.__name__, -1))
                        up(1)
                        solution.append((up.__name__, 1))
                        right(-1)
                        solution.append((right.__name__, -1))
                        left(1)
                        solution.append((left.__name__, 1))
                        up(-1)
                        solution.append((up.__name__, -1))
                        right(1) 
                        solution.append((right.__name__, 1))
                        up(2)
                        solution.append((up.__name__, 2))
                        left(-1)
                        solution.append((left.__name__, -1))
                        up(2)
                        solution.append((up.__name__, 2))
                        right(-1)
                        solution.append((right.__name__, -1))
                        up(1) #auf
                        solution.append((up.__name__, 1))
                edgestate = (state[10][1]==10, state[11][1]==11, state[7][1]==7, state[8][1]==8, state[9][1]==9) 

                    

            
        #case2: two edges adjacent are solved (only needs RUF)
        elif edgestate in edgecases2:
            print('edgecases 2')
            if edgestate == edgecases2[0]:
                moveset = (9, 6, 10)
            elif edgestate == edgecases2[1]:
                moveset = (8, 6, 9)
            elif edgestate == edgecases2[2]: 
                moveset = (7, 6, 8)
            elif edgestate == edgecases2[3]:
                moveset = (11, 6, 7)
            else:
                moveset = (10, 6, 11)
            right = moves[moveset[0]]
            up = moves[moveset[1]]
            front = moves[moveset[2]]
            
            while edgestate != (1, 1, 1, 1, 1): 
                print(edgestate)
                thing.print_state()
                print("looping")
                right(1)
                solution.append((right.__name__, 1))
                up(1)
                solution.append((up.__name__, 1))
                right(-1)
                solution.append((right.__name__, -1))
                front(-1)
                solution.append((front.__name__, -1))
                right(1)
                solution.append((right.__name__, 1))
                up(1)
                solution.append((up.__name__, 1))
                right(-1)
                solution.append((right.__name__, -1))
                up(-1)
                solution.append((up.__name__, -1))
                right(-1)
                solution.append((right.__name__, -1))
                front(1)
                solution.append((front.__name__, 1))
                right(2)
                solution.append((right.__name__, 2))
                up(-1)
                solution.append((up.__name__, -1))
                right(-1)
                solution.append((right.__name__, -1))
                # up(-1) #auf
                # solution.append((up.__name__, -1))

                maxmatches = 0
                bestrotations = 0
                edgestate = (state[10][1]==10, state[11][1]==11, state[7][1]==7, state[8][1]==8, state[9][1]==9) 

                if edgestate == (1, 1, 1, 1, 1):
                    break
                for i in range(5): #loop through 5 rotations
                    print(edgestate)
                    count = sum(bool(x) for x in edgestate)
                    
                    if count>maxmatches:
                        maxmatches = count
                        bestrotations = i
                    if edgestate == (1, 1, 1, 1, 1):
                        break
                    thing.gray6(1)
                    edgestate = (state[10][1]==10, state[11][1]==11, state[7][1]==7, state[8][1]==8, state[9][1]==9)
                thing.gray6(bestrotations)
                solution.append((thing.gray6.__name__, bestrotations))
                edgestate = (state[10][1]==10, state[11][1]==11, state[7][1]==7, state[8][1]==8, state[9][1]==9)
                print("using this edgestate")
                print(edgestate)
                if edgestate in edgecases2:
                    if edgestate == edgecases2[0]:
                        moveset = (9, 6, 10)
                    elif edgestate == edgecases2[1]:
                        moveset = (8, 6, 9)
                    elif edgestate == edgecases2[2]: 
                        moveset = (7, 6, 8)
                    elif edgestate == edgecases2[3]:
                        moveset = (11, 6, 7)
                    else:
                        moveset = (10, 6, 11)
                    right = moves[moveset[0]]
                    up = moves[moveset[1]]
                    front = moves[moveset[2]]
                elif edgestate in edgecases1:
                    print("entering the weird thing")
                    if edgestate == edgecases2[0]:
                        moveset = (9, 6, 10)
                    elif edgestate == edgecases2[1]:
                        moveset = (8, 6, 9)
                    elif edgestate == edgecases2[2]: 
                        moveset = (7, 6, 8)
                    elif edgestate == edgecases2[3]:
                        moveset = (11, 6, 7)
                    else:
                        moveset = (10, 6, 11)
                    right = moves[moveset[0]]
                    up = moves[moveset[1]]

                    solution.append((right.__name__, 1))
                    up(1)
                    solution.append((up.__name__, 1))
                    right(-1)
                    solution.append((right.__name__, -1))
                    front(-1)
                    solution.append((front.__name__, -1))
                    right(1)
                    solution.append((right.__name__, 1))
                    up(1)
                    solution.append((up.__name__, 1))
                    right(-1)
                    solution.append((right.__name__, -1))
                    up(-1)
                    solution.append((up.__name__, -1))
                    right(-1)
                    solution.append((right.__name__, -1))
                    front(1)
                    solution.append((front.__name__, 1))
                    right(2)
                    solution.append((right.__name__, 2))
                    up(-1)
                    solution.append((up.__name__, -1))
                    right(-1)
                    solution.append((right.__name__, -1))
                    # up(-1) #auf
                    # solution.append((up.__name__, -1))
                elif(edgestate == (1, 1, 1, 1, 1)):
                    break
                else:
                    edgecases = [(0, 1, 0, 0, 0),
                                (1, 0, 0, 0, 0),
                                (0, 0, 0, 0, 1),
                                (0, 0, 0, 1, 0),
                                (0, 0, 1, 0, 0)]
                    if edgestate in edgecases:
                        print(edgestate)
                        if edgestate == edgecases[0]:
                            print("enter case 0 ")
                            moveset = (9, 6, 10, 11)
                        elif edgestate == edgecases[1]:
                            moveset = (8, 6, 9, 10)
                        elif edgestate == edgecases[2]: 
                            moveset = (7, 6, 8, 9)
                        elif edgestate == edgecases[3]:
                            moveset = (11, 6, 7, 8)
                        else:
                            moveset = (10, 6, 11, 7)
                        right = moves[moveset[0]]
                        up = moves[moveset[1]]
                        front = moves[moveset[2]]
                        left = moves[moveset[3]]
                        
                        left(1)
                        solution.append((left.__name__, 1))
                        right(1)
                        solution.append((right.__name__, 1))
                        up(2)
                        solution.append((up.__name__, 2))
                        left(-1)
                        solution.append((left.__name__, -1))
                        up(1)
                        solution.append((up.__name__, 1))
                        right(-1)
                        solution.append((right.__name__, -1))
                        left(1)
                        solution.append((left.__name__, 1))
                        up(-1)
                        solution.append((up.__name__, -1))
                        right(1) 
                        solution.append((right.__name__, 1))
                        up(2)
                        solution.append((up.__name__, 2))
                        left(-1)
                        solution.append((left.__name__, -1))
                        up(2)
                        solution.append((up.__name__, 2))
                        right(-1)
                        solution.append((right.__name__, -1))
                        up(1) #auf
                        solution.append((up.__name__, 1))
                edgestate = (state[10][1]==10, state[11][1]==11, state[7][1]==7, state[8][1]==8, state[9][1]==9) 
                    
                    
        else:
            print(edgestate)
            print("no way you screwed up again")
    elif maxmatches == 1:
        #case3: one edge is solved (uses RUF + L)
        print("max matches = 1")
        edgecases = [(0, 1, 0, 0, 0),
                     (1, 0, 0, 0, 0),
                     (0, 0, 0, 0, 1),
                     (0, 0, 0, 1, 0),
                     (0, 0, 1, 0, 0)]
        if edgestate in edgecases:
            print(edgestate)
            if edgestate == edgecases[0]:
                print("enter case 0 ")
                moveset = (9, 6, 10, 11)
            elif edgestate == edgecases[1]:
                moveset = (8, 6, 9, 10)
            elif edgestate == edgecases[2]: 
                moveset = (7, 6, 8, 9)
            elif edgestate == edgecases[3]:
                moveset = (11, 6, 7, 8)
            else:
                moveset = (10, 6, 11, 7)
            right = moves[moveset[0]]
            up = moves[moveset[1]]
            front = moves[moveset[2]]
            left = moves[moveset[3]]
            
            left(1)
            solution.append((left.__name__, 1))
            right(1)
            solution.append((right.__name__, 1))
            up(2)
            solution.append((up.__name__, 2))
            left(-1)
            solution.append((left.__name__, -1))
            up(1)
            solution.append((up.__name__, 1))
            right(-1)
            solution.append((right.__name__, -1))
            left(1)
            solution.append((left.__name__, 1))
            up(-1)
            solution.append((up.__name__, -1))
            right(1) 
            solution.append((right.__name__, 1))
            up(2)
            solution.append((up.__name__, 2))
            left(-1)
            solution.append((left.__name__, -1))
            up(2)
            solution.append((up.__name__, 2))
            right(-1)
            solution.append((right.__name__, -1))
            up(1) #auf
            solution.append((up.__name__, 1))
            edgestate = (state[10][1]==10, state[11][1]==11, state[7][1]==7, state[8][1]==8, state[9][1]==9)
            thing.print_state()
            
        else:
            print("??????????? wtf")
    else: 
        #you did something wrong or edges are already permuted
        if maxmatches == 5:
            print(edgestate)
            print("edges already permuted")
        else:   
            print(maxmatches)
            print("bruh what are you doing")
    if edgestate != (True, True, True, True, True):
        print("\n")
        print(edgestate)
        raise Exception ("hi you screwed up")
    thing.print_state()
    # print(solution)
        
    #CORNER PERMUTATION
    #check state as is (no rotations)
    #case1: 3 adjacent corners solved
    #case2: 2 adjacent and 1 across corner solved
    print("DOING CORNER PERMUTATION")
    cornerstate = (thing.state[10][0]==10, thing.state[10][2]==10, thing.state[11][0]==11, thing.state[11][2]==11, thing.state[7][0]==7, thing.state[7][2]==7, thing.state[8][0]==8, thing.state[8][2]==8, thing.state[9][0]==9, thing.state[9][2]==9)
    print(cornerstate)
    cornercases1 = [(0, 1, 1, 1, 1, 0, 0, 0, 0, 0),
                    (0, 0, 0, 1, 1, 1, 1, 0, 0, 0),
                    (0, 0, 0, 0, 0, 1, 1, 1, 1, 0),
                    (1, 0, 0, 0, 0, 0, 0, 1, 1, 1),
                    (1, 1, 1, 0, 0, 0, 0, 0, 0, 1)]
    cornercases2 = [(1, 0, 0, 1, 1, 0, 0, 0, 0, 1),
                    (0, 1, 1, 0, 0, 1, 1, 0, 0, 0),
                    (0, 0, 0, 1, 1, 0, 0, 1, 1, 0),
                    (1, 0, 0, 0, 0, 1, 1, 0, 0, 1),
                    (1, 0, 0, 0, 0, 1, 1, 0, 0, 1),
                    (0, 1, 1, 0, 0, 0, 0, 1, 1, 0)]
    cornercases3 = [(0, 1, 1, 0, 0, 0, 0, 0, 0, 0),
                    (1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
                    (0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
                    (0, 0, 0, 0, 0, 1, 1, 0, 0, 0),
                    (0, 0, 0, 1, 1, 0, 0, 0, 0, 0)]
    cornercases4 = [(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)]
    
    print(cornerstate in cornercases2)
    
    thing2 = thing.__copy__()       
    while((thing.state!=thing.solved) or (thing2.state != thing2.solved)):
        print("loop")
        print("permuting corners")
        if cornerstate in cornercases1:
            print("cornercases1")
            if cornerstate == cornercases1[0]:
                moveset = (10, 9, 8) #F R BR
            elif cornerstate == cornercases1[1]:
                moveset = (11, 10, 9)
            elif cornerstate == cornercases1[2]:
                moveset = (7, 11, 10)
            elif cornerstate == cornercases1[3]:
                moveset = (8, 7, 11)
            else:
                moveset = (9, 8, 7)

            front = moves[moveset[0]]
            right = moves[moveset[1]]
            br = moves[moveset[2]]

            right(-1)
            solution.append((right.__name__, -1))
            br(-1)
            solution.append((br.__name__, -1))
            right(1)
            solution.append((right.__name__, 1))
            br(1)
            solution.append((br.__name__, 1))
            right(-1)
            solution.append((right.__name__, -1))
            front(-1)
            solution.append((front.__name__, -1))
            right(1)
            solution.append((right.__name__, 1))
            br(-1)
            solution.append((br.__name__, -1))
            right(-1)
            solution.append((right.__name__, -1))
            br(1)
            solution.append((br.__name__, 1))
            front(1)
            solution.append((front.__name__, 1))
            right(1)
            solution.append((right.__name__, 1))

        elif cornerstate in cornercases2:
            print("cornercases2")
            if cornerstate == cornercases2[0]:
                moveset = (6, 11, 9, 8) #U L R BR
            elif cornerstate == cornercases2[1]:
                moveset = (6, 7, 10, 9)
            elif cornerstate == cornercases2[2]:
                moveset = (6, 8, 11, 10)
            elif cornerstate == cornercases2[3]:
                moveset = (6, 9, 7, 11)
            else:
                moveset = (6, 10, 8, 7)

            up = moves[moveset[0]]
            left = moves[moveset[1]]
            right = moves[moveset[2]]
            br = moves[moveset[3]]

            br(-1)
            solution.append((br.__name__, -1))
            right(-1)
            solution.append((right.__name__, -1))
            up(1)
            solution.append((up.__name__, 1))
            left(1)
            solution.append((left.__name__, 1))
            up(-1)
            solution.append((up.__name__, -1))
            right(-1)
            solution.append((right.__name__, -1))
            up(1)
            solution.append((up.__name__, 1))
            left(-1)
            solution.append((left.__name__, -1))
            up(-1)
            solution.append((up.__name__, -1))
            right(2)
            solution.append((right.__name__, 2))
            br(1)
            solution.append((br.__name__, 1))

        elif cornerstate in cornercases3:
            print("cornercases3") 
            thing.print_state()
            solution2 = []
            
            moves = [thing.white0, thing.red1, thing.darkblue2, thing.yellow3, thing.purple4, thing.darkgreen5, thing.gray6, thing.orange7, thing.lightblue8, thing.cream9, thing.pink10, thing.lightgreen11]
            
            movesets = [(10, 11, 7, 8, 9), (9, 10, 11, 7, 8), (8, 9, 10, 11, 7), (7, 8, 9, 10, 11), (11, 7, 8, 9, 10)]
            for m in movesets:
                solution2 = []
                front = moves[m[0]]
                left = moves[m[1]]
                bl = moves[m[2]]
                br = moves[m[3]]
                right = moves[m[4]]
                up = moves[6]
                print("case1")
                up(1)
                solution2.append((up.__name__, 1))
                left(-1)
                solution2.append((left.__name__, -1))
                right(1)
                solution2.append((right.__name__, 1))
                up(2)
                solution2.append((up.__name__, 2))
                right(-1)
                solution2.append((right.__name__, -1))
                up(-1)
                solution2.append((up.__name__, -1))
                right(1)
                solution2.append((right.__name__, 1))
                up(1)
                solution2.append((up.__name__, 1))
                right(-1)
                solution2.append((right.__name__, -1))
                up(-1)
                solution2.append((up.__name__, -1))
                right(1)
                solution2.append((right.__name__, 1))
                up(1)
                solution2.append((up.__name__, 1))
                right(-1)
                solution2.append((right.__name__, -1))
                up(-1)
                solution2.append((up.__name__, -1))
                right(1)
                solution2.append((right.__name__, 1))
                up(-1)
                solution2.append((up.__name__, -1))
                right(-1)
                solution2.append((right.__name__, -1))
                left(1)
                solution2.append((left.__name__, 1))
                up(-1)
                solution2.append((up.__name__, -1))

                thing.print_state()
                #if solved break out of loop
                if(thing.state == thing.solved):
                    for s in solution2:
                        solution.append(s)
                    print("solved")
                    return solution
                else:
                    solution2 = []
                    up(1)
                    left(-1)
                    right(1)
                    up(1)
                    right(-1)
                    up(1)
                    right(1)
                    up(-1)
                    right(-1)
                    up(1)
                    right(1)
                    up(-1)
                    right(-1)
                    up(1)
                    right(1)
                    up(-2)
                    right(-1)
                    left(1)
                    up(-1)

                #case2
                print("case2")
                right(1)
                solution2.append((right.__name__, 1))
                up(1)
                solution2.append((up.__name__, 1))
                right(-1)
                solution2.append((right.__name__, -1))
                up(1)
                solution2.append((up.__name__, 1))
                right(-1)
                solution2.append((right.__name__, -1))
                up(-1)
                solution2.append((up.__name__, -1))
                right(1)
                solution2.append((right.__name__, 1))
                front(-1)
                solution2.append((front.__name__, -1))
                right(1)
                solution2.append((right.__name__, 1))
                up(1)
                solution2.append((up.__name__, 1))
                right(-1)
                solution2.append((right.__name__, -1))
                up(-1)
                solution2.append((up.__name__, -1))
                right(-1)
                solution2.append((right.__name__, -1))
                front(1)
                solution2.append((front.__name__, 1))
                right(2)
                solution2.append((right.__name__, 2))
                up(-1)
                solution2.append((up.__name__, -1))
                right(-2)
                solution2.append((right.__name__, -2))
                up(1)
                solution2.append((up.__name__, 1))
                right(1)
                solution2.append((right.__name__, 1))
                up(-1)
                solution2.append((up.__name__, -1))
                #if solved break out of loop
                if(thing.state == thing.solved):
                    for s in solution2:
                        solution.append(s)
                    print("solved")
                    return solution
                else:
                    solution2 = []
                    up(1)
                    right(-1)
                    up(-1)
                    right(2)
                    up(1)
                    right(-2)
                    front(-1)
                    right(1)
                    up(1)
                    right(1)
                    up(-1)
                    right(-1)
                    front(1)
                    right(-1)
                    up(1)
                    right(1)
                    up(-1)
                    right(1)
                    up(-1)
                    right(-1)


                #case3
                print("case3")
                right(2)
                solution2.append((right.__name__, 2))
                up(1)
                solution2.append((up.__name__, 1))
                right(-1)
                solution2.append((right.__name__, -1))
                up(-1)
                solution2.append((up.__name__, -1))
                ############## y ################
                br(1)
                solution2.append((br.__name__, 1))
                up(1)
                solution2.append((up.__name__, 1))
                br(-1)
                solution2.append((br.__name__, -1))
                up(-1) 
                solution2.append((up.__name__, -1))
                br(1) 
                solution2.append((br.__name__, 1))
                up(1) 
                solution2.append((up.__name__, 1))
                br(-1) 
                solution2.append((br.__name__, -1))
                up(-1)
                solution2.append((up.__name__, -1))
                br(1)
                solution2.append((br.__name__, 1))
                up(1)
                solution2.append((up.__name__, 1))
                br(-1)
                solution2.append((br.__name__, -1))
                ############# y' ################
                right(1)
                solution2.append((right.__name__, 1))
                up(-1)
                solution2.append((up.__name__, -1))
                right(-2)
                solution2.append((right.__name__, -2))
                #if solved break out of loop
                if(thing.state == thing.solved):
                    for s in solution2:
                        solution.append(s)
                    print("solved")
                    return solution
                else:
                    solution2 = []
                    right(2)
                    up(1)
                    right(-1)
                    br(1)
                    up(-1)
                    br(-1)
                    up(1)
                    br(1)
                    up(-1)
                    br(-1)
                    up(1)
                    br(1)
                    up(-1)
                    br(-1)
                    up(1)
                    right(1)
                    up(-1)
                    right(-2)
            print('done going through cornercases3')
            thing.print_state()
            raise Exception("check state")
        
        elif cornerstate in cornercases4:
            print("cornercases4")
            thing2 = thing.__copy__()
            solution2 = []
            moves = [thing.white0, thing.red1, thing.darkblue2, thing.yellow3, thing.purple4, thing.darkgreen5, thing.gray6, thing.orange7, thing.lightblue8, thing.cream9, thing.pink10, thing.lightgreen11]
            movesets = [(10, 11, 7, 8, 9), (9, 10, 11, 7, 8), (8, 9, 10, 11, 7), (7, 8, 9, 10, 11), (11, 7, 8, 9, 10)]

        
            for m in movesets:
                thing2 = thing.__copy__()
                solution2 = []
                f = moves[m[0]]
                l = moves[m[1]]
                bl = moves[m[2]]
                br = moves[m[3]]
                r = moves[m[4]]
                u = moves[6]
                
                #case1
                print("case1")

                f(1)
                solution2.append((f.__name__, 1))
                r(1)
                solution2.append((r.__name__, 1))
                u(2)
                solution2.append((u.__name__, 2))
                r(-1)
                solution2.append((r.__name__, -1))
                u(-1)
                solution2.append((u.__name__, -1))
                r(1)
                solution2.append((r.__name__, 1))
                u(-1)
                solution2.append((u.__name__, -1))
                r(-1)
                solution2.append((r.__name__, -1))
                f(-1)
                solution2.append((f.__name__, -1))
                r(-1)
                solution2.append((r.__name__, -1))
                ############## y' ################
                f(-1)
                solution2.append((f.__name__, -1))
                u(-1)
                solution2.append((u.__name__, -1))
                f(1)
                solution2.append((f.__name__, 1))
                u(-1)
                solution2.append((u.__name__, -1))
                f(-1)
                solution2.append((f.__name__, -1))
                u(2)
                solution2.append((u.__name__, 2))
                f(1)
                solution2.append((f.__name__, 1))
                r(1)
                solution2.append((r.__name__, 1))
                u(-1)
                solution2.append((u.__name__, -1))
                #if solved break out of loop
                if(thing.state == thing.solved):
                    for s in solution2:
                        solution.append(s)
                    print("solved")
                    return solution
                else:
                    solution2 = []
                    u(1)
                    r(-1)
                    f(-1)
                    u(-2)
                    f(1)
                    u(1)
                    f(-1)
                    u(1)
                    f(1)
                    r(1)
                    f(1)
                    r(1)
                    u(1)
                    r(-1)
                    u(1)
                    r(1)
                    u(-2)
                    r(-1)
                    f(-1)

                #case2
                print("case2")

                r(1)
                solution2.append((r.__name__, 1))
                u(1)
                solution2.append((u.__name__, 1))
                r(-1)
                solution2.append((r.__name__, -1))
                u(1)
                solution2.append((u.__name__, 1))
                r(-1)
                solution2.append((r.__name__, -1))
                u(-1)
                solution2.append((u.__name__, -1))
                r(2)
                solution2.append((r.__name__, 2))
                u(-1)
                solution2.append((u.__name__, -1))
                r(-1)
                solution2.append((r.__name__, -1))
                u(1)
                solution2.append((u.__name__, 1))
                r(-1)
                solution2.append((r.__name__, -1))
                u(1)
                solution2.append((u.__name__, 1))
                r(1)
                solution2.append((r.__name__, 1))
                u(1)
                solution2.append((u.__name__, 1))
                r(1)
                solution2.append((r.__name__, 1))
                u(1)
                solution2.append((u.__name__, 1))
                r(-1)
                solution2.append((r.__name__, -1))
                u(1)
                solution2.append((u.__name__, 1))
                r(-1)
                solution2.append((r.__name__, -1))
                u(-1)
                solution2.append((u.__name__, -1))
                r(2)
                solution2.append((r.__name__, 2))
                u(-1)
                solution2.append((u.__name__, -1))
                r(-1)
                solution2.append((r.__name__, -1))
                u(1)
                solution2.append((u.__name__, 1))
                r(-1)
                solution2.append((r.__name__, -1))
                u(1)
                solution2.append((u.__name__, 1))
                r(1)
                solution2.append((r.__name__, 1))
                u(1)
                solution2.append((u.__name__, 1))

                #if solved break out of loop
                if(thing.state == thing.solved):
                    for s in solution2:
                        solution.append(s)
                    print("solved")
                    return solution
                else:
                    solution2 = []
                    u(-1)
                    r(-1)
                    u(-1)
                    r(1)
                    u(-1)
                    r(1)
                    u(1)
                    r(-2)
                    u(1)
                    r(1)
                    u(-1)
                    r(1)
                    u(-1)
                    r(-1)
                    u(-1)
                    r(-1)
                    u(-1)
                    r(1)
                    u(-1)
                    r(1)
                    u(1)
                    r(-2)
                    u(1)
                    r(1)
                    u(-1)
                    r(1)
                    u(-1)
                    r(-1)
                    

                #case3
                print("case3")

                r(2)
                solution2.append((r.__name__, 2))
                u(2)
                solution2.append((u.__name__, 2))
                r(-2)
                solution2.append((r.__name__, -2))
                u(-1)
                solution2.append((u.__name__, -1))
                r(2)
                solution2.append((r.__name__, 2))
                u(-1)
                solution2.append((u.__name__, -1))
                r(-2)
                solution2.append((r.__name__, -2))
                ########## y' ###########
                f(-2)
                solution2.append((f.__name__, -2))
                u(-1)
                solution2.append((u.__name__, -1))
                f(2)
                solution2.append((f.__name__, 2))
                u(-1)
                solution2.append((u.__name__, -1))
                f(-2)
                solution2.append((f.__name__, -2))
                u(2)
                solution2.append((u.__name__, 2))
                f(2)
                solution2.append((f.__name__, 2))
                u(-1)
                solution2.append((u.__name__, -1))

                #if solved break out of loop
                if(thing.state == thing.solved):
                    for s in solution2:
                        solution.append(s)
                    print("solved")
                    return solution
                else:
                    solution2 = []
                    u(1)
                    f(-2)
                    u(-2)
                    f(2)
                    u(1)
                    f(-2)
                    u(1)
                    f(2)
                    r(2)
                    u(1)
                    r(-2)
                    u(1)
                    r(2)
                    u(-2)
                    r(-2)

                #case4
                print("case4")

                r(-2)
                solution2.append((r.__name__, -2))
                u(-2)
                solution2.append((u.__name__, -2))
                r(2)
                solution2.append((r.__name__, 2))
                u(1)
                solution2.append((u.__name__, 1))
                r(-2)
                solution2.append((r.__name__, -2))
                u(1)
                solution2.append((u.__name__, 1))
                r(2)
                solution2.append((r.__name__, 2))
                ############## y ################
                br(2)
                solution2.append((br.__name__, 2))
                u(1)
                solution2.append((u.__name__, 1))
                br(-2)
                solution2.append((br.__name__, -2))
                u(1)
                solution2.append((u.__name__, 1))
                br(2)
                solution2.append((br.__name__, 2))
                u(-2)
                solution2.append((u.__name__, -2))
                br(-2)
                solution2.append((br.__name__, -2))
                u(1)
                solution2.append((u.__name__, 1))
                #if solved break out of loop
                if(thing.state == thing.solved):
                    for s in solution2:
                        solution.append(s)
                    print("solved")
                    return solution
                else:
                    solution2 = []
                    u(-1)
                    br(2)
                    u(2)
                    br(-2)
                    u(-1)
                    br(2)
                    u(-1)
                    br(-2)
                    r(-2)
                    u(-1)
                    r(2)
                    u(-1)
                    r(-2)
                    u(2)
                    r(2)

                #case5
                print("case5")

                r(2)
                solution2.append((r.__name__, 2))
                u(-2)
                solution2.append((u.__name__, -2))
                r(-2)
                solution2.append((r.__name__, -2))
                u(-1)
                solution2.append((u.__name__, -1))
                r(2)
                solution2.append((r.__name__, 2))
                u(-2)
                solution2.append((u.__name__, -2))
                r(-1)
                solution2.append((r.__name__, -1))
                u(1)
                solution2.append((u.__name__, 1))
                r(-1)
                solution2.append((r.__name__, -1))
                u(-1)
                solution2.append((u.__name__, -1))
                r(-1)
                solution2.append((r.__name__, -1))
                f(1)
                solution2.append((f.__name__, 1))
                r(2)
                solution2.append((r.__name__, 2))
                u(-1)
                solution2.append((u.__name__, -1))
                r(-1)
                solution2.append((r.__name__, -1))
                u(-1)
                solution2.append((u.__name__, -1))
                r(1)
                solution2.append((r.__name__, 1))
                u(1)
                solution2.append((u.__name__, 1))
                r(-1)
                solution2.append((r.__name__, -1))
                f(-1)
                solution2.append((f.__name__, -1))

                #if solved break out of loop
                if(thing.state == thing.solved):
                    for s in solution2:
                        solution.append(s)
                    print("solved")
                    return solution
                else:
                    solution2 = []
                    f(1)
                    r(1)
                    u(-1)
                    r(-1)
                    u(1)
                    r(1)
                    u(1)
                    r(-2)
                    f(-1)
                    r(1)
                    u(1)
                    r(1)
                    u(-1)
                    r(1)
                    u(2)
                    r(-2)
                    u(1)
                    r(2)
                    u(2)
                    r(-2)

                #case6
                print("case6")
                
                r(-1)
                solution2.append((r.__name__, -1))
                u(2)
                solution2.append((u.__name__, 2))
                r(1)
                solution2.append((r.__name__, 1))
                u(-1)
                solution2.append((u.__name__, -1))
                r(-1)
                solution2.append((r.__name__, -1))
                u(2)
                solution2.append((u.__name__, 2))
                r(1)
                solution2.append((r.__name__, 1))
                u(-2)
                solution2.append((u.__name__, -2))
                r(-1)
                solution2.append((r.__name__, -1))
                u(-1)
                solution2.append((u.__name__, -1))
                r(1)
                solution2.append((r.__name__, 1))
                u(-2)
                solution2.append((u.__name__, -2))
                r(-1)
                solution2.append((r.__name__, -1))
                u(1)
                solution2.append((u.__name__, 1))
                r(1)
                solution2.append((r.__name__, 1))
                u(-2)
                solution2.append((u.__name__, -2))
                r(-1)
                solution2.append((r.__name__, -1))
                u(1)
                solution2.append((u.__name__, 1))
                r(1)
                solution2.append((r.__name__, 1))

                #if solved break out of loop
                if(thing.state == thing.solved):
                    for s in solution2:
                        solution.append(s)
                    print("solved")
                    return solution
                else:
                    solution2 = []
                    r(-1)
                    u(-1)
                    r(1)
                    u(2)
                    r(-1)
                    u(-1)
                    r(1)
                    u(2)
                    r(-1)
                    u(1)
                    r(1)
                    u(2)
                    r(-1)
                    u(-2)
                    r(1)
                    u(1)
                    r(-1)
                    u(-2)
                    r(1)

                #case7
                print("case7")

                r(2)
                solution2.append((r.__name__, 2))
                u(-2)
                solution2.append((u.__name__, -2))
                r(-2)
                solution2.append((r.__name__, -2))
                u(-1)
                solution2.append((u.__name__, -1))
                r(2)
                solution2.append((r.__name__, 2))
                u(1)
                solution2.append((u.__name__, 1))
                r(-2)
                solution2.append((r.__name__, -2))
                u(-1)
                solution2.append((u.__name__, -1))
                r(2)
                solution2.append((r.__name__, 2))
                u(1)
                solution2.append((u.__name__, 1))
                r(-2)
                solution2.append((r.__name__, -2))
                u(-1)
                solution2.append((u.__name__, -1))
                r(2)
                solution2.append((r.__name__, 2))
                u(-2)
                solution2.append((u.__name__, -2))
                r(-2)
                solution2.append((r.__name__, -2))

                #if solved break out of loop
                if(thing.state == thing.solved):
                    for s in solution2:
                        solution.append(s)
                    print("solved")
                    return solution
                else:
                    solution2 = []
                    r(2)
                    u(2)
                    r(-2)
                    u(1)
                    r(2)
                    u(-1)
                    r(-2)
                    u(1)
                    r(2)
                    u(-1)
                    r(-2)
                    u(1)
                    r(2)
                    u(2)
                    r(-2)

                #case8
                print("case8")

                r(2)
                solution2.append((r.__name__, 2))
                u(2)
                solution2.append((u.__name__, 2))
                r(-2)
                solution2.append((r.__name__, -2))
                u(1)
                solution2.append((u.__name__, 2))
                r(2)
                solution2.append((r.__name__, 2))
                u(-1)
                solution2.append((u.__name__, -1))
                r(-2)
                solution2.append((r.__name__, -2))
                u(1)
                solution2.append((u.__name__, 1))
                r(2)
                solution2.append((r.__name__, 2))
                u(-1)
                solution2.append((u.__name__, -1))
                r(-2)
                solution2.append((r.__name__, -2))
                u(1)
                solution2.append((u.__name__, 1))
                r(2)
                solution2.append((r.__name__, 2))
                u(2)
                solution2.append((u.__name__, 2))
                r(-2)
                solution2.append((r.__name__, -2))

                #if solved break out of loop
                if(thing.state == thing.solved):
                    for s in solution2:
                        solution.append(s)
                    print("solved")
                    return solution
                else:
                    solution2 = []
                    r(2)
                    u(-2)
                    r(-2)
                    u(-1)
                    r(2)
                    u(1)
                    r(-2)
                    u(-1)
                    r(2)
                    u(1)
                    r(-2)
                    u(-1)
                    r(2)
                    u(-2)
                    r(-2)

            print('done going through cornercases4')
            thing.print_state()
            raise Exception("check state")

        else:
            print("bruh")
            thing.print_state()
            if thing.state == thing.solved:
                return solution
            
    
        
        cornerstate = (thing.state[10][0]==10, thing.state[10][2]==10, thing.state[11][0]==11, thing.state[11][2]==11, thing.state[7][0]==7, thing.state[7][2]==7, thing.state[8][0]==8, thing.state[8][2]==8, thing.state[9][0]==9, thing.state[9][2]==9)
        print(cornerstate)
    if thing.state == thing.solved:
        return solution
    elif thing2.state == thing.solved:
        print("thing2 is solved")
        return solution
    else:
        return "uh oh"
        