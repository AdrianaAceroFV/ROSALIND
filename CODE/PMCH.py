#Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

#Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s

import math 

with open('rosalind_pmch.txt', 'r') as file:
    sequence = file.read()

    A = sequence.count('A')
    C = sequence.count('C')
     
    result = math.factorial(A)*math.factorial(C)
    print(result)
