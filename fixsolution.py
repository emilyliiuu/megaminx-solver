def connectsolution(solution):
    newsolution = []
    rotations = solution[0][1]
    for i in range(1, len(solution)):
        if solution[i-1][0] == solution[i][0]:
            rotations +=solution[i][1]
        else:
            newsolution.append((solution[i-1], rotations))
            rotations = solution[i][1]
    return newsolution
    



def fixsolution(solution):
    newsolution = []
    for moves in solution:
        pair = [0, 0]
        if moves[0] == 'white0':
            pair[0] = 0
        elif moves[0] == 'red1':
            pair[0] = 1
        elif moves[0] == 'darkblue2':
            pair[0] = 2
        elif moves[0] == 'yellow3':
            pair[0] = 3
        elif moves[0] == 'purple4':
            pair[0] = 4
        elif moves[0] == 'darkgreen5':
            pair[0] = 5
        elif moves[0] == 'gray6':
            pair[0] = 6
        elif moves[0] == 'orange7':
            pair[0] = 7
        elif moves[0] == 'lightblue8':
            pair[0] = 8
        elif moves[0] == 'cream9':
            pair[0] = 9
        elif moves[0] == 'pink10':
            pair[0] = 10
        elif moves[0] == 'lightgreen11':
            pair[0] = 11


        # 0 -> -2, 1 -> -1, 2 -> 1, 3 -> 2
        if moves[1] == 1:
            # pair[1] = 1
            pair[1] = 2
        elif moves[1] == 2:
            # pair[1] = 2
            pair[1] = 3
        elif moves[1] == 3:
            # pair[1] = -2
            pair[1] = 0
        elif moves[1] == 4:
            # pair[1] = -1
            pair[1] = 1
        elif moves[1] == -1:
            # pair[1] = -1
            pair[1] = 1
        elif moves[1] == -2:
            # pair[1] = -2
            pair[1] = 0
        elif moves[1] == -3:
            # pair[1] = 2
            pair[1] = 3
        elif moves[1] == -4:
            # pair[1] = 1
            pair[1] = 2
        elif moves[1] == 5:
            continue

        newsolution.append(pair)
    return newsolution
