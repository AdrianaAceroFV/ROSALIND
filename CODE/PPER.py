#Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.

#Return: The total number of partial permutations P(n,k), modulo 1,000,000.

import math 

def partial_permutations(n,k):
    result = (math.comb(n,k) * math.factorial(k))%1000000
    return print(result)

partial_permutations(89,9)
