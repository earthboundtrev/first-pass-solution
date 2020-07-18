import math
# from itertools import permutations 
# from itertools import combinations
import itertools
import ipdb

import sys

def rock_paper_scissors(n):
  # Your code here
  choices = ['rock', 'paper', 'scissors']
  
  iterating_list_counter = 0
  max_iterating_list_size = pow(3, n)
  list_to_return = [None] * max_iterating_list_size
  # choices = [1, 2, 3]
  # comb = itertools.combinations(choices, n)
  # print(list(itertools.combinations(choices, n)))
  for i in range(0, 3):
    for j in range(0, 3):
      # ipdb.set_trace()
      list_as_iterating = []
      print("This is the list before the value is updated:", list_as_iterating)
      list_as_iterating.extend((choices[i],choices[j]))
      list_to_return[iterating_list_counter] = list_as_iterating
      iterating_list_counter=iterating_list_counter+1
      print("This is the list after the value is updated:", list_as_iterating)
    
  return list_to_return

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')