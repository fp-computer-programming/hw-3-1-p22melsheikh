# Author MEE 10/4/21

t1_wins = input("How many wins does team one have? ")
t1_ties = input("How many ties does team one have? ")
t2_wins = input("How many wins does team one have? ")
t2_ties = input("How many ties does team one have? ")

t1_pts = (int(t1_wins) * 3) + (int(t1_ties))
t2_pts = (int(t2_wins) * 3) + (int(t2_ties))

t1_pts = (int(t1_wins) * 3) + (int(t1_ties))
t2_pts = (int(t2_wins) * 3) + (int(t2_ties))
if t1_pts < t2_pts:
    print(" Team 2 wins")
else:
    print("team 1 wins")
