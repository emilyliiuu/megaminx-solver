from minx import Minx
from lastlayer import lastlayer

thing = Minx()
solution = []

br = thing.lightblue8
r = thing.cream9
u = thing.gray6
l = thing.lightgreen11
f = thing.pink10

if thing.state == thing.solved:
    print("this is valid")

#test 2 adjacent 1 across corner permutation
#WORKS!!!!!!!!!!
br(-1)
r(-1)
u(1)
l(1)
u(-1)
r(-1)
u(1)
l(-1)
u(-1)
r(2)
br(1)
# thing.print_state()
# solution = lastlayer(thing, solution)
# thing.print_state()
# print(solution)


# #test 3 adjacent corner permutation
# #WORKS!!!!!!!!!!!!!!!!!!!!!!!!!
# r(-1)
# br(-1)
# r(1)
# br(1)
# r(-1)
# f(-1)
# r(1)
# br(-1)
# r(-1)
# br(1)
# f(1)
# r(1)
# thing.print_state()
# solution = lastlayer(thing, solution)
# thing.print_state()
# print(solution)

#test complex corner permutation
# #last case on minx ll doc
# #unsolvable using two algs
# r(2)
# u(2)
# r(-2)
# u(1)
# r(2)
# u(-1)
# r(-2)
# u(1)
# r(2)
# u(-1)
# r(-2)
# u(1)
# r(2)
# u(2)
# r(-2)
# thing.print_state()
# solution = lastlayer(thing, solution)
# thing.print_state()
# print(solution)
# #INFINITE LOOPING

# #complex corner permutation
# #rotation case 2
# #WORKSSSS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# r(1)
# u(1)
# r(-1)
# u(1)
# r(-1)
# u(-1)
# r(2)
# u(-1)
# r(-1)
# u(1)
# r(-1)
# u(1)
# r(1)
# u(1)
# r(1)
# u(1)
# r(-1)
# u(1)
# r(-1)
# u(-1)
# r(2)
# u(-1)
# r(-1)
# u(1)
# r(-1)
# u(1)
# r(1)
# u(1)
# # thing.print_state()
# # solution = lastlayer(thing, solution)
# # thing.print_state()
# # print(solution)

# #test edge permutation case 1
# #WORKS!!!!!!!!!!!!!!
# r(2)
# u(-2)
# r(-2)
# u(-1)
# r(2)
# u(-2)
# r(-2)
# thing.print_state()
# solution = lastlayer(thing, solution)
# thing.print_state()
# print(solution)

# #test edge permutation case 2
# #WORKS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
# r(1)
# u(1)
# r(-1)
# f(-1)
# r(1)
# u(1)
# r(-1)
# u(-1)
# r(-1)
# f(1)
# r(2)
# u(-1)
# r(-1)
# thing.print_state()
# solution = lastlayer(thing, solution)
# thing.print_state()
# print(solution)

#test edge permutation case 3
#WORKS!!!!!!!!!!!!
l(1)
r(1)
u(2)
l(-1)
u(1)
r(-1)
l(1)
u(-1)
r(1)
u(2)
l(-1)
u(2)
r(-1)
# thing.print_state()
# solution = lastlayer(thing, solution)
# thing.print_state()
# print(solution)

#test corner ORIENTATION case 4
#WORKS!!!!!!!!!!!!!!!!!!1
r(1)
u(1)
r(-1)
u(1)
r(1)
u(1)
r(-1)
u(-2)
r(1)
u(-1)
r(-1)
# thing.print_state()
# solution = lastlayer(thing, solution)
# thing.print_state()
# print(solution) 

# #test corner ORIENTATION case 
# #WORKS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# r(1)
# u(1)
# r(-1)
# u(1)
# r(1)
# u(1)
# r(-1)
# u(-1)
# r(1)
# u(-2)
# r(-1)
# thing.print_state()
# solution = lastlayer(thing, solution)
# thing.print_state()
# print(solution) 

# #test EDGE ORIENTATION case 1
# #WORKS!!!!!!!!!!1
# f(1)
# r(1)
# u(1)
# r(-1)
# u(-1)
# r(1)
# u(1)
# r(-1)
# u(-1)
# f(-1)
# thing.print_state()
# solution = lastlayer(thing, solution)
# thing.print_state()
# print(solution) 

#test EDGE ORIENTATION case 2
#WORKS!!!!!!!!!!!!!!!!!!!!!!!!1
f(1)
r(1)
u(1)
r(-1)
u(-1)
f(-1)
# thing.print_state()
# solution = lastlayer(thing, solution)
# thing.print_state()
# print(solution) 

# #test EDGE ORIENTATION case 3
# #WORKS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# f(1)
# r(1)
# u(2)
# r(-2)
# f(1)
# r(1)
# f(-1)
# u(-2)
# f(-1)
# thing.print_state()
# solution = lastlayer(thing, solution)
# thing.print_state()
# print(solution) 

#test entire last layer
thing.print_state()
solution = lastlayer(thing, solution)
thing.print_state()
print(solution)
#WORKS!!!!!!!!!!!!!!!!!!!1


