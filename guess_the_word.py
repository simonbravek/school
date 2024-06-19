import sys
import os

def get_single_char():
    if os.name == 'nt':  # Windows
        import msvcrt
        char = msvcrt.getch()
        return char.decode()
    else:  # Unix-like systems (Linux, macOS)
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            char = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return char
    
def get_onetime_char():
    while True:
        char=get_single_char()
        if char.isalpha():
            if char not in have:
                return char
        

def print_word_status(target):
    for word in puzzle.split():
        for letter in list(word):
            if letter in target:
                print(letter, end="")
            else:
                print(".", end="")
        print(" ", end="")
    print("\n")

def print_guess_status(target):
    for letter in target:
        print(letter, end=" ")
    print("\n")

def print_remainer(tries, round):
    print(f"You have {tries-round} more attempts.\n")


puzzle=input("\nPick a puzzle for others. Do not show or tell them.: ")
puzzle_chars = list(puzzle.replace(" ", ""))
print()
have=[]
tries=10
round=0

while round < tries:
    miss=[]
    for letter in have:
        if letter not in puzzle_chars:
            miss.append(letter)
    round=len(miss)

    print_word_status(have)
    print_guess_status(miss)
    print_remainer(tries, round)
    char=get_onetime_char()
    have.append(char)
    win=all(letter in have for letter in puzzle_chars)
    if win==True:
        print("YOU WIN")
        break


print("THE END")