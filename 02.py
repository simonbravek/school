import time
import sys

def print_and_overwrite(string1, string2):
  """Prints the given string to the terminal and then overwrites it with the other given string.

  Args:
    string1: The first string to print.
    string2: The second string to overwrite the first string with.
  """

  sys.stdout.write(string1)
  sys.stdout.flush()
  sys.stdout.write("\033[0K")
  sys.stdout.write(string2)
  sys.stdout.flush()

list_1 = [2]
dir = 0 # 0 is right, 1 is down, 2 is laft, 3 is up
x = 5
y = 5

print("Hello")


#for i in range(20):
    #time.sleep(1)
    # print("XXXXXXXXXXXXXXXXXXXX\nX                  X\nX                  X\nX                  X\nX                  X\nX                  X\nX                  X\nX                  X\nX                  X\nXXXXXXXXXXXXXXXXXXXX")
