from minx import Minx

thing = Minx()
thing2 = thing.__copy__()


thing2.white0(1)
thing.print_state()
print("\n")
thing2.print_state()
print("\n")

thing2 = thing.__copy__()
thing2.print_state()

