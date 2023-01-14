#A permutation of length n is an ordering of the positive integers {1,2,…,n} For example, π=(5,3,2,1,4)
#is a permutation of length 5.

#Given: A positive integer n≤7.

#Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

import itertools as it
import math

def permutation(n):
    nums = list(range(1,n+1))
    permutations = list(it.permutations(nums))
    fact = math.factorial(n)
    with open("solution19.txt","w") as solution:
        solution.write(str(fact))
        for i in permutations:
            solution.write('\n'+' '.join(map(str,i)))
    solution.close()
  
  #writing the solution in a txt file