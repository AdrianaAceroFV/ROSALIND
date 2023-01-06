#Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. 
#Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

#Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). 
#Assume that Mendel's second law holds for the factors.

import math

def probability(k,N):
    p = 0.25
    prob = 0
    m=2**k
    while N <= m:
        prob = prob + math.comb(m,N)*(p**N)*(1-p)**(m-N) #Cumulative Binomial Distribution 
        N+=1
    return print(round(prob,3))

probability(6,18)        
