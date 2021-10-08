# Author MEE 10/4/21

c1v = input("What is the value of your first card? ")
c2v = input("What is the value of your second card? ")

if (c1v + c2v) <= 21:
    print("You are safe")
else:
    print("You are busted")