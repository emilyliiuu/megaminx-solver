import random
import numpy as np
import copy

class Minx:
  #ALL MOVES WORK
  #EDGE/CORNER MAPPING DONE
  #NEED TO TEST EDGE/CORNER MAPPING

  def __init__(self):
    self.color_codes = {
        0: "white",
        1: "red",
        2: "darkblue",
        3: "yellow",
        4: "purple",
        5: "darkgreen",
        6: "gray",
        7: "orange",
        8: "lightblue",
        9: "cream",
        10: "pink",
        11: "lightgreen"
    }
    self.adj_num = {
        0: [4, 5, 1, 2, 3],
        1: [0, 5, 9, 10, 2],
        2: [0, 1, 10, 11, 3],
        3: [0, 2, 11, 7, 4],
        4: [0, 3, 7, 8, 5],
        5: [0, 4, 8, 9, 1],
        6: [10, 9, 8, 7, 11],
        7: [6, 8, 4, 3, 11],
        8: [6, 9, 5, 4, 7],
        9: [6, 10, 1, 5, 8],
        10: [6, 11, 2, 1, 9],
        11: [6, 7, 3, 2, 10]
    }
    self.adj_let = {
        0: ["E", "F", "B", "C", "D"],
        1: ["A", "F", "J", "K", "C"],
        2: ["A", "B", "K", "L", "D"],
        3: ["A", "C", "L", "H", "E"],
        4: ["A", "D", "H", "I", "F"],
        5: ["A", "E", "I", "J", "B"],
        6: ["K", "J", "I", "H", "L"],
        7: ["G", "I", "E", "D", "L"],
        8: ["G", "J", "F", "E", "H"],
        9: ["G", "K", "B", "F", "I"],
        10: ["G", "L", "C", "B", "J"],
        11: ["G", "H", "D", "C", "K"]
    }
    self.state = {
        0: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        1: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        2: [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        3: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        4: [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        5: [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        6: [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        7: [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
        8: [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
        9: [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        10: [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        11: [11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
    }
    self.solved = {
        0: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        1: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        2: [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        3: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        4: [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        5: [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        6: [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        7: [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
        8: [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
        9: [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        10: [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        11: [11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
    }
    self.edges = { 
      #white edges
      (0, 4) : (self.state[0][1], self.state[4][1]) , #white purple
      (0, 5) : (self.state[0][3], self.state[5][1]), #white darkgreen
      (0, 1) : (self.state[0][5], self.state[1][1]), #white red
      (0, 2) : (self.state[0][7], self.state[2][1]), #white darkblue
      (0, 3) : (self.state[0][9], self.state[3][1]), #white yellow

      #next layer
      (3, 4)  : (self.state[3][9], self.state[4][3]), #yellow purple
      (4, 5) : (self.state[4][9], self.state[5][3]), #purple darkgreen
      (5, 1) : (self.state[5][9], self.state[1][3]), #green red
      (1, 2) : (self.state[1][9], self.state[2][3]), #red darkblue
      (2, 3) : (self.state[2][9], self.state[3][3]), #darkblue yellow
      
      #next layer
      (3, 11) : (self.state[3][5], self.state[11][5]), #yellow lightgreen
      (3, 7) : (self.state[3][7], self.state[11][7]), #yellow orange
      (4, 7) : (self.state[4][5], self.state[7][5]), #purple orange
      (4, 8) : (self.state[4][7], self.state[8][7]), #purple lightblue
      (5, 8) : (self.state[5][5], self.state[8][5]), #darkgreen lightblue
      (5, 9) : (self.state[5][7], self.state[9][7]), #darkgreen cream
      (1, 9) : (self.state[1][5], self.state[9][5]), #red cream
      (1, 10) : (self.state[1][7], self.state[10][7]), #red pink
      (2, 10) : (self.state[2][5], self.state[10][5]), #darkblue pink
      (2, 11) : (self.state[2][7], self.state[11][7]), #darkblue lightgreen

      #next layer
      (11, 7) : (self.state[11][3], self.state[7][9]), #lightgreen orange
      (7, 8) : (self.state[7][3], self.state[8][9]), #orange lightblue
      (8, 9) : (self.state[8][3], self.state[9][9]), #lightblue cream
      (9, 10) : (self.state[9][3], self.state[10][9]), #cream pink
      (10, 11) : (self.state[10][3], self.state[11][9]), #pink lightgreen

      #gray edges #edges are wrong!!
      (6, 10) : (self.state[6][1], self.state[10][1]), #gray pink
      (6, 11) : (self.state[6][9], self.state[11][1]), #gray lightgreen
      (6, 7) : (self.state[6][7], self.state[7][1]), #gray orange
      (6, 8) : (self.state[6][5], self.state[8][1]), #gray lightblue
      (6, 9) : (self.state[6][3], self.state[9][1]), #gray cream
    }
    self.corners = {
      #white corners
      (0, 3, 4) : (self.state[0][0], self.state[3][0], self.state[4][2]), #white yellow purple
      (0, 4, 5) : (self.state[0][2], self.state[4][0], self.state[5][2]), #white purple darkgreen
      (0, 5, 1) : (self.state[0][4], self.state[5][0], self.state[1][2]), #white darkgreen red
      (0, 1, 2) : (self.state[0][6], self.state[1][0], self.state[2][2]), #white red darkblue
      (0, 2, 3) : (self.state[0][8], self.state[2][0], self.state[3][2]), #white darkblue yellow

      #next layer
      (3, 7, 4) : (self.state[3][8], self.state[7][6], self.state[4][4]), #yellow orange purple
      (7, 8, 4) : (self.state[7][4], self.state[8][8], self.state[4][6]), #orange lightblue purple
      (4, 8, 5) : (self.state[4][8], self.state[8][6], self.state[5][4]), #purple lightblue darkgreen
      (8, 9, 5) : (self.state[8][4], self.state[9][8], self.state[5][6]), #lightblue cream darkgreen
      (5, 9, 1) : (self.state[5][8], self.state[9][6], self.state[1][4]), #darkgreen cream red
      (9, 10, 1) : (self.state[9][4], self.state[10][8], self.state[1][6]), #cream pink red
      (1, 10, 2) : (self.state[1][8], self.state[10][6], self.state[2][4]), #red pink darkblue
      (10, 11, 2) : (self.state[10][4], self.state[11][8], self.state[2][6]), #pink lightgreen darkblue
      (2, 11, 3) : (self.state[2][8], self.state[11][6], self.state[3][4]), #darkblue lightgreen yellow
      (11, 7, 3) : (self.state[11][4], self.state[7][8], self.state[3][6]), #lightgreen orange yellow

      #gray corners
      (6, 11, 10) : (self.state[6][0], self.state[11][0], self.state[10][2]), #gray lightgreen pink
      (6, 10, 9) : (self.state[6][2], self.state[10][0], self.state[9][2]), #gray pink cream
      (6, 9, 8) : (self.state[6][4], self.state[9][0], self.state[8][2]), #gray cream lightblue
      (6, 8, 7) : (self.state[6][6], self.state[8][0], self.state[7][2]), #gray lightblue orange
      (6, 7, 11) : (self.state[6][8], self.state[7][0], self.state[11][2])#gray orange lightgreen
    }
  
  def update_edges(self):
      self.edges = { 
      #white edges
      (0, 4) : (self.state[0][1], self.state[4][1]) , #white purple
      (0, 5) : (self.state[0][3], self.state[5][1]), #white darkgreen
      (0, 1) : (self.state[0][5], self.state[1][1]), #white red
      (0, 2) : (self.state[0][7], self.state[2][1]), #white darkblue
      (0, 3) : (self.state[0][9], self.state[3][1]), #white yellow

      #next layer
      (3, 4)  : (self.state[3][9], self.state[4][3]), #yellow purple
      (4, 5) : (self.state[4][9], self.state[5][3]), #purple darkgreen
      (5, 1) : (self.state[5][9], self.state[1][3]), #darkgreen red
      (1, 2) : (self.state[1][9], self.state[2][3]), #red darkblue
      (2, 3) : (self.state[2][9], self.state[3][3]), #darkblue yellow
      
      #next layer
      (3, 11) : (self.state[3][5], self.state[11][5]), #yellow lightgreen
      (3, 7) : (self.state[3][7], self.state[7][7]), #yellow orange
      (4, 7) : (self.state[4][5], self.state[7][5]), #purple orange
      (4, 8) : (self.state[4][7], self.state[8][7]), #purple lightblue
      (5, 8) : (self.state[5][5], self.state[8][5]), #darkgreen lightblue
      (5, 9) : (self.state[5][7], self.state[9][7]), #darkgreen cream
      (1, 9) : (self.state[1][5], self.state[9][5]), #red cream
      (1, 10) : (self.state[1][7], self.state[10][7]), #red pink
      (2, 10) : (self.state[2][5], self.state[10][5]), #darkblue pink
      (2, 11) : (self.state[2][7], self.state[11][7]), #darkblue lightgreen

      #next layer
      (11, 7) : (self.state[11][3], self.state[7][9]), #lightgreen orange
      (7, 8) : (self.state[7][3], self.state[8][9]), #orange lightblue
      (8, 9) : (self.state[8][3], self.state[9][9]), #lightblue cream
      (9, 10) : (self.state[9][3], self.state[10][9]), #cream pink
      (10, 11) : (self.state[10][3], self.state[11][9]), #pink lightgreen

      #gray edges
      (6, 10) : (self.state[6][1], self.state[10][1]), #gray pink
      (6, 11) : (self.state[6][9], self.state[11][1]), #gray lightgreen
      (6, 7) : (self.state[6][7], self.state[7][1]), #gray orange
      (6, 8) : (self.state[6][5], self.state[8][1]), #gray lightblue
      (6, 9) : (self.state[6][3], self.state[9][1]), #gray cream
    }
    
  def update_corners(self):
    self.corners = {
      #white corners
      (0, 3, 4) : (self.state[0][0], self.state[3][0], self.state[4][2]), #white yellow purple
      (0, 4, 5) : (self.state[0][2], self.state[4][0], self.state[5][2]), #white purple darkgreen
      (0, 5, 1) : (self.state[0][4], self.state[5][0], self.state[1][2]), #white darkgreen red
      (0, 1, 2) : (self.state[0][6], self.state[1][0], self.state[2][2]), #white red darkblue
      (0, 2, 3) : (self.state[0][8], self.state[2][0], self.state[3][2]), #white darkblue yellow

      #next layer
      (3, 7, 4) : (self.state[3][8], self.state[7][6], self.state[4][4]), #yellow orange purple
      (7, 8, 4) : (self.state[7][4], self.state[8][8], self.state[4][6]), #orange lightblue purple
      (4, 8, 5) : (self.state[4][8], self.state[8][6], self.state[5][4]), #purple lightblue darkgreen
      (8, 9, 5) : (self.state[8][4], self.state[9][8], self.state[5][6]), #lightblue cream darkgreen
      (5, 9, 1) : (self.state[5][8], self.state[9][6], self.state[1][4]), #darkgreen cream red
      (9, 10, 1) : (self.state[9][4], self.state[10][8], self.state[1][6]), #cream pink red
      (1, 10, 2) : (self.state[1][8], self.state[10][6], self.state[2][4]), #red pink darkblue
      (10, 11, 2) : (self.state[10][4], self.state[11][8], self.state[2][6]), #pink lightgreen darkblue
      (2, 11, 3) : (self.state[2][8], self.state[11][6], self.state[3][4]), #darkblue lightgreen yellow
      (11, 7, 3) : (self.state[11][4], self.state[7][8], self.state[3][6]), #lightgreen orange yellow

      #gray corners
      (6, 11, 10) : (self.state[6][0], self.state[11][0], self.state[10][2]), #gray lightgreen pink
      (6, 10, 9) : (self.state[6][2], self.state[10][0], self.state[9][2]), #gray pink cream
      (6, 9, 8) : (self.state[6][4], self.state[9][0], self.state[8][2]), #gray cream lightblue
      (6, 8, 7) : (self.state[6][6], self.state[8][0], self.state[7][2]), #gray lightblue orange
      (6, 7, 11) : (self.state[6][8], self.state[7][0], self.state[11][2])#gray orange lightgreen
    }
  
  def set_state(self, new_state):
    self.state = new_state
    self.edges = { 
      #white edges
      (0, 4) : (self.state[0][1], self.state[4][1]) , #white purple
      (0, 5) : (self.state[0][3], self.state[5][1]), #white darkgreen
      (0, 1) : (self.state[0][5], self.state[1][1]), #white red
      (0, 2) : (self.state[0][7], self.state[2][1]), #white darkblue
      (0, 3) : (self.state[0][9], self.state[3][1]), #white yellow

      #next layer
      (3, 4)  : (self.state[3][9], self.state[4][3]), #yellow purple
      (4, 5) : (self.state[4][9], self.state[5][3]), #purple darkgreen
      (5, 1) : (self.state[5][9], self.state[1][3]), #darkgreen red
      (1, 2) : (self.state[1][9], self.state[2][3]), #red darkblue
      (2, 3) : (self.state[2][9], self.state[3][3]), #darkblue yellow
      
      #next layer
      (3, 11) : (self.state[3][5], self.state[11][5]), #yellow lightgreen
      (3, 7) : (self.state[3][7], self.state[7][7]), #yellow orange
      (4, 7) : (self.state[4][5], self.state[7][5]), #purple orange
      (4, 8) : (self.state[4][7], self.state[8][7]), #purple lightblue
      (5, 8) : (self.state[5][5], self.state[8][5]), #darkgreen lightblue
      (5, 9) : (self.state[5][7], self.state[9][7]), #darkgreen cream
      (1, 9) : (self.state[1][5], self.state[9][5]), #red cream
      (1, 10) : (self.state[1][7], self.state[10][7]), #red pink
      (2, 10) : (self.state[2][5], self.state[10][5]), #darkblue pink
      (2, 11) : (self.state[2][7], self.state[11][7]), #darkblue lightgreen

      #next layer
      (11, 7) : (self.state[11][3], self.state[7][9]), #lightgreen orange
      (7, 8) : (self.state[7][3], self.state[8][9]), #orange lightblue
      (8, 9) : (self.state[8][3], self.state[9][9]), #lightblue cream
      (9, 10) : (self.state[9][3], self.state[10][9]), #cream pink
      (10, 11) : (self.state[10][3], self.state[11][9]), #pink lightgreen

      #gray edges
      (6, 10) : (self.state[6][1], self.state[10][1]), #gray pink
      (6, 11) : (self.state[6][9], self.state[11][1]), #gray lightgreen
      (6, 7) : (self.state[6][7], self.state[7][1]), #gray orange
      (6, 8) : (self.state[6][5], self.state[8][1]), #gray lightblue
      (6, 9) : (self.state[6][3], self.state[9][1]), #gray cream
    }
    self.corners = {
      #white corners
      (0, 3, 4) : (self.state[0][0], self.state[3][0], self.state[4][2]), #white yellow purple
      (0, 4, 5) : (self.state[0][2], self.state[4][0], self.state[5][2]), #white purple darkgreen
      (0, 5, 1) : (self.state[0][4], self.state[5][0], self.state[1][2]), #white darkgreen red
      (0, 1, 2) : (self.state[0][6], self.state[1][0], self.state[2][2]), #white red darkblue
      (0, 2, 3) : (self.state[0][8], self.state[2][0], self.state[3][2]), #white darkblue yellow

      #next layer
      (3, 7, 4) : (self.state[3][8], self.state[7][6], self.state[4][4]), #yellow orange purple
      (7, 8, 4) : (self.state[7][4], self.state[8][8], self.state[4][6]), #orange lightblue purple
      (4, 8, 5) : (self.state[4][8], self.state[8][6], self.state[5][4]), #purple lightblue darkgreen
      (8, 9, 5) : (self.state[8][4], self.state[9][8], self.state[5][6]), #lightblue cream darkgreen
      (5, 9, 1) : (self.state[5][8], self.state[9][6], self.state[1][4]), #darkgreen cream red
      (9, 10, 1) : (self.state[9][4], self.state[10][8], self.state[1][6]), #cream pink red
      (1, 10, 2) : (self.state[1][8], self.state[10][6], self.state[2][4]), #red pink darkblue
      (10, 11, 2) : (self.state[10][4], self.state[11][8], self.state[2][6]), #pink lightgreen darkblue
      (2, 11, 3) : (self.state[2][8], self.state[11][6], self.state[3][4]), #darkblue lightgreen yellow
      (11, 7, 3) : (self.state[11][4], self.state[7][8], self.state[3][6]), #lightgreen orange yellow

      #gray corners
      (6, 11, 10) : (self.state[6][0], self.state[11][0], self.state[10][2]), #gray lightgreen pink
      (6, 10, 9) : (self.state[6][2], self.state[10][0], self.state[9][2]), #gray pink cream
      (6, 9, 8) : (self.state[6][4], self.state[9][0], self.state[8][2]), #gray cream lightblue
      (6, 8, 7) : (self.state[6][6], self.state[8][0], self.state[7][2]), #gray lightblue orange
      (6, 7, 11) : (self.state[6][8], self.state[7][0], self.state[11][2])#gray orange lightgreen
    }


  def __copy__(self):
    thing2 = Minx()
    # for i in range(0, len(self.state)):
    #   for j in range(0, len(self.state[0])):
    #     thing2.state[i][j] = self.state[i][j]
    state2 = copy.deepcopy(self.state)
    thing2.state = state2
    return thing2

  def rotate_matrix(self, color, direction):
    arr = np.array(self.state[color])
    if direction == 1:
      rotated_array = np.roll(arr, -2)
    else:
      rotated_array = np.roll(arr, 2)

    self.state[color] = rotated_array.tolist()
    self.update_edges()
    self.update_corners()

  def print_state(self):
    for i in range(0, 12):
      print(self.state[i])

  def changeState(self, numRotations, adj_n, to_replace):

    after = []
    #print(to_replace)
    for i in range(0, 5):
      next = adj_n[(i - numRotations) % 5]
      after = to_replace[i] + self.state[next][3:]
      self.state[next] = after

  def moveU(self, top, numRotations):
    count = abs(numRotations)
    adj_n = self.adj_num[top]  #second?
    to_replace = []
    for i in range(5):
      to_replace.append(self.state[adj_n[i]][:3])
    
    self.changeState(numRotations, adj_n, to_replace)
    for j in range(count):
      self.rotate_matrix(top, numRotations/abs(numRotations))
    
    self.update_edges()
    self.update_corners()

  def moveUp(self, top, numRotations):
    self.moveU(top, -1 * numRotations)
  
  def rotation(self, numRotations, adj_n, first_segment, first_idx):
    to_replace = [first_segment]
    for j in range(1, 5):
      currstate = self.state[adj_n[j]][:]
      segment = []
      if j == 1:
        segment = currstate[-2:] + currstate[0:1]
        #print(segment)
      elif j == 2:
        segment = currstate[4:7]
      elif j == 3:
        segment = currstate[6:9]
      else:
        segment = currstate[2:5]
      to_replace = to_replace + [segment]

    direction = 1 if numRotations > 0 else -1

    for i in range(0, 5):
      if (i == 0):
        if ((first_idx + 3) % 10 < first_idx):  #only one possible case here
          

          after = to_replace[(i+direction)%5][-1:] + self.state[
              adj_n[0]][1:8] + to_replace[(i+direction)%5][0:2]  
        else:
          after = self.state[adj_n[0]][0:first_idx] + to_replace[
              (i + direction) % 5] + self.state[adj_n[0]][first_idx + 3:]
      elif (i == 1):
        after = to_replace[(i + direction) % 5][-1:] + self.state[
            adj_n[1]][1:8] + to_replace[(i + direction) % 5][0:2]
      elif (i == 2):
        after = self.state[adj_n[2]][:4] + to_replace[
            (i + direction) % 5] + self.state[adj_n[2]][-3:]
      elif (i == 3):
        after = self.state[adj_n[3]][:6] + to_replace[
            (i + direction) % 5] + self.state[adj_n[3]][-1:]
      else:
        after = self.state[adj_n[4]][:2] + to_replace[
            (i + direction) % 5] + self.state[adj_n[4]][-5:]
      #print(after)
      self.state[adj_n[i]] = after

  def moveF(self, top, numRotations):
    #if white top then purple adjacency, if gray top then pink adjacency
    adj_n = self.adj_num[4] if top == 0 else self.adj_num[10]
    count = abs(numRotations)
    for j in range(count):
      first_segment = self.state[adj_n[0]][0:3]
      self.rotation(numRotations, adj_n, first_segment, 0)
    for i in range(count):
      if top ==0:
        self.rotate_matrix(4, numRotations/abs(numRotations))
      else:
        self.rotate_matrix(10, numRotations/abs(numRotations))
          
    self.update_edges()
    self.update_corners()


  def moveFp(self, top, numRotations):
    self.moveF(top, -1 * numRotations)

  def moveR(self, top, numRotations):
    #if white top then darkgreen adjacency, if gray top then cream adjacency
    adj_n = self.adj_num[5] if top == 0 else self.adj_num[9]
    count = abs(numRotations)
    for j in range(count):
      first_segment = self.state[adj_n[0]][2:5]
      self.rotation(numRotations, adj_n, first_segment, 2)
    for i in range(count):
      if top == 0:
        self.rotate_matrix(5, numRotations/abs(numRotations))
      else:
        self.rotate_matrix(9, numRotations/abs(numRotations))
          
    self.update_edges()
    self.update_corners()
      

  def moveRp(self, top, numRotations):
    self.moveR(top, -1 * numRotations)

  def moveL(self, top, numRotations):
    #if white top then yellow adjacency, if gray top then lightgreen adjacency
    adj_n = self.adj_num[3] if top == 0 else self.adj_num[11]
    count = abs(numRotations)
    for j in range(count):
      first_segment = self.state[adj_n[0]][-2:] + self.state[adj_n[0]][0:1]
      #first_segment = self.state[adj_n[0]][9:] + self.state[adj_n[0]][0:1]
      
      #print(first_segment)
      self.rotation(numRotations, adj_n, first_segment, 9)
    for i in range(count):
      if top ==0:
        self.rotate_matrix(3, numRotations/abs(numRotations))
      else:
        self.rotate_matrix(11, numRotations/abs(numRotations))
          
          
    self.update_edges()
    self.update_corners()
    

  def moveLp(self, top, numRotations):
    self.moveL(top, -1 * numRotations)

  def moveBR(self, top, numRotations):
    #if white top then red adjacency, if gray top then light blue adjacency
    adj_n = self.adj_num[1] if top == 0 else self.adj_num[8]
    count = abs(numRotations)
    for i in range (count):
      first_segment = self.state[adj_n[0]][4:7]
      self.rotation(numRotations, adj_n, first_segment, 4)
    for j in range(count):
      if top ==0:
        self.rotate_matrix(1, numRotations/abs(numRotations))
      else:
        #print("enter")
        self.rotate_matrix(8, numRotations/abs(numRotations))
          
    self.update_edges()
    self.update_corners()
    

  def moveBRp(self, top, numRotations):
    self.moveBR(top, -1 * numRotations)
    
  def moveBL(self, top, numRotations):      
    #if white top then dark blue adjacency, if gray top then orange adjacency
    adj_n = self.adj_num[2] if top == 0 else self.adj_num[7]
    count = abs(numRotations)
    for j in range(count):
      first_segment = self.state[adj_n[0]][6:9]
      self.rotation(numRotations, adj_n, first_segment, 6)
    for i in range(count):
      if top ==0:
        self.rotate_matrix(2, numRotations/abs(numRotations))
      else:
        self.rotate_matrix(7, numRotations/abs(numRotations))
          
    self.update_edges()
    self.update_corners()

  def moveBLp(self, top, numRotations):     
    self.moveBL(top, -1 * numRotations)

  def white0(self, dir): #dir is 1 when cw, -1 when ccw
    self.moveU(0, dir)

  def red1(self, dir):
    self.moveBR(0, dir)

  def darkblue2(self, dir):
    self.moveBL(0, dir)

  def yellow3(self, dir):
    self.moveL(0, dir)

  def purple4(self, dir):
    self.moveF(0, dir)

  def darkgreen5(self, dir):
    self.moveR(0, dir)

  def gray6(self, dir):
    self.moveU(6, dir)

  def orange7(self, dir):
    self.moveBL(6, dir)

  def lightblue8(self, dir):
    self.moveBR(6, dir)

  def cream9(self, dir):
    self.moveR(6, dir)

  def pink10(self, dir):
    self.moveF(6, dir)

  def lightgreen11(self, dir):
    self.moveL(6, dir)
    
  def scramble(self):
    scramblemoves = []
    n = [-2, 2] #using double moves results in a better scramble than using a mix of single and double moves

    moves = [self.white0, self.red1, self.darkblue2, self.yellow3, self.purple4, self.darkgreen5, 
             self.gray6, self.orange7, self.lightblue8, self.cream9, self.pink10, self.lightgreen11]
    for i in range(0, 50):  #official scramble length idk
      move = random.choice(moves)
      rotations = random.choice(n)
      move(rotations)
      scramblemoves.append((move.__name__, rotations))
    self.update_edges()
    self.update_corners()
    return scramblemoves

  def reset(self):
    self.state = self.solved
    self.update_edges()
    self.update_corners()