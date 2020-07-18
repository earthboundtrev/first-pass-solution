import math
# from itertools import permutations 
# from itertools import combinations
import itertools
#!/usr/bin/python


import sys

def rock_paper_scissors(n):
  # Your code here
  choices = ['rock', 'paper', 'scissors']
  # choices = [1, 2, 3]
  # comb = itertools.combinations(choices, n)
  # print(list(itertools.combinations(choices, n)))
  for index in range(0, n+1):
      comb = itertools.combinations(['rock', 'paper', 'scissors'], index)
      for i in list(comb):
          perm = itertools.permutations(i)
          for j in list(perm):
              print(j)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')