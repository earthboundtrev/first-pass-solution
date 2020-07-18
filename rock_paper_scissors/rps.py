import math
# from itertools import permutations 
# from itertools import combinations
import itertools
import ipdb

import sys

def rock_paper_scissors(n):
  # Your code here
  choices = ['rock', 'paper', 'scissors']
  counter_list [0] * n
  counter1=0
  counter2=0
  iterating_list_counter = 0
  max_iterating_list_size = pow(3, n)
  list_to_return = [None] * max_iterating_list_size
  # choices = [1, 2, 3]
  # comb = itertools.combinations(choices, n)
  # print(list(itertools.combinations(choices, n)))
  for i in range(0, max_iterating_list_size):
      list_to_iterate=[]
      list_to_iterate.extend((choices[counter1], choices[counter2]))
      if(counter2 < n):
          counter2=counter2+1
      else:
          counter1=counter1+1
          counter2=0
      list_to_return[iterating_list_counter] = list_to_iterate
      iterating_list_counter=iterating_list_counter+1
      
    
  return list_to_return

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')