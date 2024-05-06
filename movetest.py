from minx import Minx
from whitestar import white_star

thing = Minx()
thing2 = Minx()
""" 
#test double moves
thing.print_state()
print("\n")
thing.moveU(0,2)
thing2.moveU(0, 1)
thing2.moveU(0,1) 
thing.print_state()
print("\n")
thing2.print_state()
"""
"""
#test other moves
#thing.print_state()
thing.moveFp(0, 1)
#thing.print_state()
print("\n")
thing.moveFp(0, 1)
#thing.print_state()
print("\n")
thing2.moveFp(0, 2)
thing.print_state()
print("\n")
thing2.print_state()
"""

# #test move equivalents
# thing.red1(-1)
# thing.print_state()
# print("\n")

# thing2.moveBR(0, -1)
# thing2.print_state()

"""
#test scramble
thing.scramble()
thing.print_state()
"""

#test multiple moves
thing.red1(2)
thing.darkblue2(3)
thing.yellow3(1)
thing.purple4(1)
thing.darkgreen5(1)
thing.gray6(2)
thing.orange7(2)
thing.lightblue8(-1)
thing.cream9(1)
thing.pink10(1)
thing.lightgreen11(1)
thing.print_state()

