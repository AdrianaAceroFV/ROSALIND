#Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

#Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).

with open("rosalind_lexf.txt", "r") as file: 
    data = file.read().replace("\n", " ").split()
    data[-1] = int(data[-1])

import itertools as it
import math

r = [perm for perm in it.product(data[:-1], repeat =data[-1])]

sols = list(map("".join, r))
print(*sols,sep='\n')