#Interaktivni verze
#verze PvE

import random, time, sys

random_int = random.randrange(0, 100)

print("------------------------------------------------")
print("I think a number from 0 to 100. I bet you can't guess...")
time.sleep(1)
print("-- Do you want to want to continue? --  (y/n) ", end="")
time.sleep(1)
init = input("\r                                              ")

if init != "y":
    print("Maybe later")
    sys.exit()

print("\rI will guess it!")
host_guess = input("This is my first guess: ")

while True:
    if int(host_guess) < random_int:
        print("Too low")
    elif int(host_guess) > random_int:
        print("Too high")
    elif int(host_guess) == random_int:
        print("You are the best!")
        time.sleep(1)
        print("\n(\   /)\n(´•ᴥ•`)\n ૮♡૮ )\n")
        sys.exit()
    host_guess = input("So let's try: ")