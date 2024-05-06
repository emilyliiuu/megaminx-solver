from minx import Minx
from whitestar import white_star

thing = Minx()

#test scramble/reset
# print("scramble + reset")
# thing.scramble()
# #thing.print_state()
# print(thing.edges)
# print(len(thing.edges))
# print("\n")
# thing.reset()
# thing.print_state()

#test case 0
# thing.white0(4)
# sol = white_star(thing)
# print(sol)

'''
#test case 1
print("\ncase 1")
thing.darkgreen5(1)
# thing.red1(1)
# thing.purple4(-1)
thing.print_state()
print(thing.edges)
print("\n")
sol = white_star(thing)
thing.print_state()
print("\n")
print(sol)
'''

'''
#test case 2
print("\ncase2 ")
# ALL THESE CASES WORK!!!
# thing.white0(2)
# thing.purple4(2)
# thing.white0(-2)  

# thing.white0(-1)
# thing.darkblue2(-1)
# thing.white0(1)

# thing.red1(-2)
# thing.cream9(1)
# thing.pink10(3)
# thing.lightgreen11(2)

# thing.white0(-1)
# thing.yellow3(2)
# thing.orange7(1)
# thing.white0(1)


thing.print_state()
print(thing.edges)
print("\n")
sol = white_star(thing)
thing.print_state()
print("\n")
print(sol)
'''

# #test case 3
# print("\ncase3 ")
# #displace 4 cross pieces WORKS!!!!!
# thing.red1(1)
# thing.white0(1)
# thing.red1(-1)
# thing.white0(-1)
# thing.darkblue2(2)
# thing.lightgreen11(1)
# thing.yellow3(-1)
# thing.purple4(2)

# thing.print_state()
# sol = white_star(thing)
# thing.print_state()
# print("\n")
# print(sol)


# #test case 4 
# #WORKS!!!!!!!!!1
# print("\ncase4 ")
# thing.red1(2)
# thing.pink10(-2)
# thing.print_state()
# print("\n")
# sol = white_star(thing)
# thing.print_state()
# print("\n")
# print(sol)


#test case 5
#WORKS!!!!!!!!!!!!!!!
# print("\ncase2 ")
# thing.darkblue2(-2)
# thing.pink10(-1)
# thing.red1(-1)
# thing.darkblue2(1)
# thing.red1(1)
# thing.print_state()
# print("\n")
# sol = white_star(thing)
# thing.print_state()
# print("\n")
# print(sol)



#test entire white cross
scramble = thing.scramble()
print("scramble\n")
print(scramble)
print("\n")
thing.print_state()
print("\n")
sol = white_star(thing)
thing.print_state()
print("\n")
print(sol)


'''
moving a piece in case 2 while switching idx when white is on white adj will break a cross piece. must move it back before doing next thing
having edge piece on gray face was fixed by switching idx, prob should check if this breaks anything as well.
'''
